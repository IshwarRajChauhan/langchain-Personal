import datetime

from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import HumanMessage
from langchain_core.output_parsers.openai_tools import (
    JsonOutputKeyToolsParser, PydanticToolsParser)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

from schemas import AnswerQuestion, ReviseAnswer

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0, max_tokens=4096)
parser = JsonOutputKeyToolsParser(key_name="AnswerQuestion", return_id=True)
parser_pydantic = PydanticToolsParser(tools=[AnswerQuestion])


actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert researcher.
Current time: {time}

1. {first_instruction}
2. Reflect and critique your answer. Be severe to maximize improvement.
3. Recommend search queries to research information and improve your answer.

You MUST respond only by calling the provided tool/function with these fields filled in.
Do NOT write your answer as plain text or markdown. Do NOT respond outside the tool call.""",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
).partial(time=lambda: datetime.datetime.now().isoformat())


first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction="Provide a detailed 250 word answer."
)


first_responder = first_responder_prompt_template | llm.bind_tools(
    tools=[AnswerQuestion], tool_choice="AnswerQuestion"
).with_retry(stop_after_attempt=5)


revise_instructions = """Revise your previous answer using the new information.
    - You should use the previous critique to add important information to your answer.
        - You MUST include numerical citations in your revised answer text so it can be verified, e.g. [1], [2].
        - Do NOT write a "References" section inside the answer text.
        - Instead, populate the separate `references` field of the tool call with the full URL for each numbered citation, e.g. ["https://example.com", "https://example2.com"].
    - You should use the previous critique to remove superfluous information from your answer and make SURE it is not more than 250 words.
"""

revisor = actor_prompt_template.partial(
    first_instruction=revise_instructions
) | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer").with_retry(stop_after_attempt=5)


if __name__ == "__main__":
    human_message = HumanMessage(
        content="Write about AI-Powered SOC / autonomous SOC problem domain,"
        " list startups that do that and raised capital."
    )

    chain = (
        first_responder_prompt_template
        | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
        | parser_pydantic
    )

    res = chain.invoke(input={"messages": [human_message]})
    print(res)
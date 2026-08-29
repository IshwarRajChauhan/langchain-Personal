import asyncio

from dotenv import load_dotenv

load_dotenv()
from langchain_core.agents import HumanMessage
from langchain_groq import ChatGroq
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain.agents import create_agent

llm = ChatGroq(model="openai/gpt-oss-120b")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/Users/chauh/OneDrive/Desktop/study/Python/Python - Gen-AI langchain_langsmith/10.MCP/servers/math_server.py"],
)


async def main():
    async with stdio_client(stdio_server_params) as (read,write):
        async with ClientSession(read_stream=read,write_stream=write ) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)
            
            agent = create_agent(llm,tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 52 + 2 * 4?")]})            
            print(result["messages"][-1].content)




if __name__ == "__main__":
    asyncio.run(main())

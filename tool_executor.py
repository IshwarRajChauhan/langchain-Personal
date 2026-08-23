from dotenv import load_dotenv

load_dotenv()

from langchain_core.tools import StructuredTool
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

from schemas import AnswerQuestion, ReviseAnswer

tavily_tool = TavilySearch(max_results=3)


def run_queries(search_queries: list[str], **kwargs):
    """Run the generated queries."""
    results = tavily_tool.batch([{"queries": query} for query in search_queries])
    # trim content to keep context small enough for free-tier TPM limits
    for r in results:
        if isinstance(r, dict) and "results" in r:
            for item in r["results"]:
                if "content" in item and item["content"]:
                    item["content"] = item["content"][:500]
    return results


execute_tools = ToolNode(
    [
        StructuredTool.from_function(run_queries, name=AnswerQuestion.__name__),
        StructuredTool.from_function(run_queries, name=ReviseAnswer.__name__),
    ]
)
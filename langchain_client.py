import asyncio

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")


async def main():
    print("Hello langchain mcp")


if __name__ == "__main__":
    asyncio.run(main())

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import json
import httpx
from bs4 import BeautifulSoup

load_dotenv()

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"
SERPER_URL = "https://google.serper.dev/search"

docs_url = {
    "langchain": "https://python.langchain.com/docs/",
    "llama-index": "https://www.llamaindex.ai/en/stable",
    "openai": "https://platform.openai.com/docs/api-reference",
    "anthropic": "https://docs.anthropic.com/en/api/reference",
    "groq": "https://docs.groq.com/api-reference",
    "mistral": "https://docs.mistral.ai/api-reference", 
}

async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q": query, "num": 3})

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(SERPER_URL, headers=headers, data=payload, timeout=20)
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            print("Timeout searching web")
            return {"organic": []}

async def fetch_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout error"


@mcp.tool()
async def get_docs(query: str, library: str):
    """
    Search the documentation for a given query and library.
    Supports the following libraries: langchain, llama-index, openai, anthropic, groq, mistral.

    Args:
        query: The query to search the documentation for example "how to use langchain".
        library: The library to search the documentation for example "langchain".

    Returns:
        Text from the documentation.
    """
    if library not in docs_url:
        raise ValueError(f"Library {library} not supported")

    query = f"site: {docs_url[library]} {query}"
    results = await search_web(query)
    if len(results["organic"]) == 0:
        return "No results found"
    
    text = ""
    for result in results["organic"]:
        text += await fetch_url(result["link"])
    return text

if __name__ == "__main__":
    mcp.run(transport="stdio")
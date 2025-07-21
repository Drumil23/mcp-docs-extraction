from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

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

def search_web():
    ...

def fetch_url():
    ...

@mcp.tool()
def get_docs():
    ...





def main():
    print("Hello from documentation!")


if __name__ == "__main__":
    main()

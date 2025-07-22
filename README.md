# Documentation MCP Server

A Model Context Protocol (MCP) server that provides intelligent documentation search capabilities for popular AI/ML libraries and frameworks.

## Overview

This MCP server enables AI assistants to search and retrieve documentation from various popular libraries including LangChain, LlamaIndex, OpenAI, Anthropic, Groq, and Mistral. It combines web search capabilities with document fetching to provide relevant documentation snippets based on user queries.

## Features

- **Multi-library Support**: Search documentation for:
  - LangChain
  - LlamaIndex  
  - OpenAI API
  - Anthropic API
  - Groq API
  - Mistral API
- **Intelligent Search**: Uses Serper API for targeted web searches within documentation sites
- **Content Extraction**: Fetches and parses HTML content to extract readable text
- **MCP Integration**: Seamlessly integrates with MCP-compatible AI assistants

## Prerequisites

- Python 3.13 or higher
- Serper API key (for web search functionality)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd documentation
   ```

2. Install dependencies using uv:
   ```bash
   uv install
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root:
   ```env
   SERPER_API_KEY=your_serper_api_key_here
   ```

2. Get a Serper API key:
   - Visit [Serper.dev](https://serper.dev)
   - Sign up for an account
   - Generate an API key
   - Add it to your `.env` file

## Usage

### Running the Server

To start the MCP server:

```bash
python main.py
```

The server will run using stdio transport, making it compatible with MCP clients.

### Available Tools

#### `get_docs`

Search documentation for a specific library and query.

**Parameters:**
- `query` (string): The search query (e.g., "how to use langchain")
- `library` (string): The target library ("langchain", "llama-index", "openai", "anthropic", "groq", or "mistral")

**Returns:**
- Text content from relevant documentation pages

**Example:**
```python
# Search for LangChain chain usage
result = await get_docs("how to create chains", "langchain")

# Search for OpenAI API reference
result = await get_docs("chat completions", "openai")
```

## Supported Libraries

| Library | Documentation URL |
|---------|------------------|
| LangChain | https://python.langchain.com/docs/ |
| LlamaIndex | https://www.llamaindex.ai/en/stable |
| OpenAI | https://platform.openai.com/docs/api-reference |
| Anthropic | https://docs.anthropic.com/en/api/reference |
| Groq | https://docs.groq.com/api-reference |
| Mistral | https://docs.mistral.ai/api-reference |

## How It Works

1. **Query Processing**: The server receives a query and target library
2. **Web Search**: Uses Serper API to search within the specified documentation site
3. **Content Fetching**: Retrieves the top 3 search results
4. **Text Extraction**: Parses HTML content using BeautifulSoup to extract readable text
5. **Response**: Returns the combined text content from all fetched pages

## Error Handling

- **Timeout Protection**: All HTTP requests have a 20-second timeout
- **Library Validation**: Ensures only supported libraries are queried
- **Graceful Failures**: Returns appropriate error messages for failed requests

## Development

### Project Structure

```
documentation/
├── main.py           # Main MCP server implementation
├── pyproject.toml    # Project configuration
├── uv.lock          # Dependency lock file
├── .env             # Environment variables (create this)
└── README.md        # This file
```

### Dependencies

- `mcp[cli]>=1.12.0` - Model Context Protocol framework
- `httpx>=0.28.1` - Async HTTP client
- `python-dotenv` - Environment variable management
- `beautifulsoup4` - HTML parsing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

1. **"No results found"**: Check your internet connection and verify the Serper API key
2. **Timeout errors**: The service may be experiencing high load; try again later
3. **Unsupported library**: Ensure you're using one of the supported library names

### API Rate Limits

Be mindful of Serper API rate limits. The free tier typically allows a limited number of searches per month.

## Support

For questions, issues, or contributions, please open an issue in the GitHub repository.
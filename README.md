# Installation

Replace or merge the following MCP server configuration into your MCP config file (for example `mcp-server.config.json` or `config.json`). Top-level key is `mcpServers`. This will start the server on your local machine.

```json
{
    "mcpServers": {
        "Demo-Github": {
            "disabled": false,
            "timeout": 60,
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/edtemboml/mcp-server-example.git",
                "mcp-server"
            ]
        }
    }
}
```

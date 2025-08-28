from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Simple Deployment")


@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

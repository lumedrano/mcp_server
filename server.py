from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool
async def add(a: int, b: int) -> int:
    """
    Adds two numbers together.
    """
    return a + b

@mcp.tool
async def greet(name: str) -> str:
    """
    returns a simple greeting using the client's name
    """
    return f"hello, {name}"

if __name__ == "__main__":
    mcp.run()
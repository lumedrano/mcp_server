from fastmcp import Client
import asyncio


async def main():
    client = Client("http://127.0.0.1:8000/mcp")
    await client._connect()

    tools = await client.list_tools()
    print(tools)

    add = await client.call_tool("add", {"a":1, "b":2})
    print(add.data)

    greet = await client.call_tool("greet", {"name": "Luigi"})
    print(greet.data)

if __name__ == "__main__":
    asyncio.run(main())
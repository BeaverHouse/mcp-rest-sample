from mcp.server.fastmcp import FastMCP
import inspect

__all__ = ['mcp']

mcp = FastMCP("Sample MCP Server, attached to the FastAPI server")

# Import all tool modules
from . import body, family, health

# Dynamically register all tools from body module
for module in [body, family, health]:
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and obj.__name__.startswith('tool_'):
            mcp.add_tool(
                name=obj.__name__,
                description=obj.__doc__,
                fn=obj
            )
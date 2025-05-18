from datetime import datetime
import os
from fastmcp import FastMCP
from zoneinfo import ZoneInfo


mcp = FastMCP(
    name="time-mcp",
    instructions="You are a helpful assistant that can answer questions about the current time in given timezone.",
    description="A simple MCP server that returns the current time in given timezone",
    version="1.0.0",
    author="Bilal Fazalani",
    author_email="bilal.m.fazlani@gmail.com",
)


@mcp.tool()
def get_current_time(timezone: str = "Asia/Kolkata") -> str:
    """
    Get the current time in the given timezone.
    If no timezone is provided, the default is Asia/Kolkata.

    Args:
        timezone: The timezone to get the current time in.

    Returns:
        The current time in the given timezone.
    """
    try:
        zone = ZoneInfo(timezone)
        return datetime.now(zone).isoformat()
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", 8000)
    mcp.run(transport="streamable-http", host=host, port=port, path="/mcp")

import asyncio
import json
import os
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, Resource

server = Server("james-skills-mcp")

@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    return [
        Tool(
            name="interactive_grill_me",
            description="Launch an interactive Grill-Me UI in Claude for a branching interview.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "The decision or plan to be grilled."}
                },
                "required": ["topic"]
            }
        ),
        Tool(
            name="interactive_baseon",
            description="Launch an interactive Base-On UI to apply a knowledge lens.",
            inputSchema={
                "type": "object",
                "properties": {
                    "lens": {"type": "string", "description": "The framework or lens to apply."}
                },
                "required": ["lens"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "interactive_grill_me":
        # In MCP Apps 2026, we return a special payload or resource URI that Claude interprets as an Interactive App.
        # We'll return an HTML payload instructing the rendering of the interactive grill-me UI.
        html_payload = """
        <div style="padding: 20px; font-family: 'IBM Plex Sans Thai', sans-serif;">
            <h2>Grill Me: Interactive Session</h2>
            <p>Topic: {topic}</p>
            <div id="grill-app"></div>
            <script>
                // PostMessage communication setup for Claude MCP Apps
                window.parent.postMessage({ type: 'mcp-app-ready', skill: 'grill-me' }, '*');
            </script>
        </div>
        """.replace("{topic}", arguments.get("topic", "Unknown"))
        
        return [TextContent(type="text", text=f"Rendering Interactive UI for Grill-Me. (MCP App Resource)\n\n```html\n{html_payload}\n```")]

    elif name == "interactive_baseon":
        return [TextContent(type="text", text="Rendering Interactive UI for Base-On.")]
    
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())

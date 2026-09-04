# Grill Me — James Edition (Public Release)

This is a stress-testing decision framework. You can install and use it in any AI assistant (ChatGPT, Claude, Gemini, Cursor).

## How to Install & Use (For General Users)
**You DO NOT need any complex setup or MCP servers.** 
1. Open the `SKILL.md` file in this folder.
2. Copy all the text inside.
3. Paste it into your AI's **"Custom Instructions"**, **"System Prompt"**, or Claude's **"Projects"** knowledge base.
4. To start using it, just type: `Grill me on my new marketing plan.`

The AI will automatically use **Text-Chat Mode** to ask you one concise question at a time until the decision tree is resolved.

## Advanced Users (Interactive UI on Claude Desktop)
If you are a power user using **Claude Desktop** and want native, clickable interactive pop-ups instead of typing in chat:
You can run the included `mcp-server` in this repository to unlock the `interactive_grill_me` UI. The skill prompt is already smart enough to detect the server and switch to Native UI automatically. If the server is offline, it gracefully falls back to text chat.

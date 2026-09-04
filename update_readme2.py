import re

with open("README.md", "r") as f:
    content = f.read()

architecture_text = """
## 🏛️ Architecture: The 3 Universal Pillars (Plugins)

JamesSkills uses a **Hybrid Plugin Architecture** to ensure compatibility across Antigravity, Claude, ChatGPT, and Cursor. The repository is divided into three distinct modules:

1. ⚙️ **`james-core`**: The foundational reasoning engine, behavioral rules (`proactive-habits`, `make-it-james`), and strict QA gates (`/are-you-sure`, `/prove-it`). *(Always On)*
2. 📊 **`james-productivity`**: Business strategy, frameworks, and executive document outputs (`/baseon`, `/one-page-pls`, `/sum-meet`). *(Toggle when doing business)*
3. 💻 **`james-software`**: Development standards, UI/UX psychological mindset (`/make-it-james-ux`), and strict coding protocols (`/proactive-dev`). *(Toggle when coding)*

**Universal Deployment:**
- **Antigravity**: Automatically mounts as 3 independent plugins via `plugin.json`, separating `rules/` (Always-On) from `skills/` (On-Demand).
- **Claude/ChatGPT**: Upload the markdown files in `skills/` to Project Knowledge, and paste `rules/` into Custom Instructions.
- **Cursor**: Reference `rules/` via `.cursorrules` and use `@` for skills on-demand.
"""

content = content.replace("## 📚 Full Skill Directory (Before vs After)", architecture_text + "\n## 📚 Full Skill Directory (Before vs After)")

with open("README.md", "w") as f:
    f.write(content)

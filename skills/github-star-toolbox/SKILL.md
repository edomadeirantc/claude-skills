---
name: github-star-toolbox
description: Load-on-demand router for 112 starred GitHub repos. Use when the user asks which starred tool/skill/MCP/app to use, where reverse-skill lives, or how to find a capability that is not in the global skill allowlist. Do not dump the catalog into the system prompt. Never install OmniRoute or 9router unless asked. reverse-skill is toolbox-only, authorized-scope only, never auto-run.
---

# GitHub Star Toolbox

Canonical catalog (read only when needed):

`C:\Users\011\.agents\toolbox\catalog.json`

Canonical skills library:

`C:\Users\011\.agents\skills`

## Rules

1. Keep this skill's prompt footprint small. Never paste the full catalog into a reply unless the user asks for the whole index.
2. To answer "do I already have X?", read `catalog.json` and filter by `kind`, `full_name`, or keywords in `description`/`notes`.
3. Global skills are already installed under `~/.agents/skills`. Plugins stay plugins. Apps/libs stay toolbox references.
4. `zhaoxuya520/reverse-skill` is **on-demand only**:
   - Path if cloned: `C:\Users\011\.agents\toolbox\repos\zhaoxuya520-reverse-skill`
   - Do **not** copy it into `~/.agents/skills` or any session skill root.
   - Do **not** execute its scripts, exploits, or scanners automatically.
   - Use only when the user explicitly requests reverse-engineering or authorized security research on systems they own or have written permission to test.
   - If scope is missing, ask for authorization before reading that repo.
5. `diegosouzapw/OmniRoute` and `decolua/9router` are catalogued as `skip_now`. Do not install.
6. Ignore `edomadeirantc/claude-mem`, `edomadeirantc/ui-ux-pro-max-skill`, and `edomadeirantc/supervision`. Use upstream.
7. Prefer existing plugins for TDD, debugging, plans, UI (superpowers, mattpocock, frontend-design, ui-ux-pro-max, ponytail).
8. Project Speckit skills stay in this repo. Do not promote them to user-global.

## How to look up

Read the catalog with a search, for example:

- kind = `mcp` for GitHub/Playwright MCP
- kind = `skill_global` for allowlisted skills
- kind = `security_ondemand` for reverse-skill
- kind = `toolbox_app` / `toolbox_lib` / `toolbox_reference` for non-skill stars

Then open only the matching `html_url` or local path.

## Install policy

Do not run third-party plugin installers or hooks from this catalog. Adding a new **global** skill requires an explicit user request and a SKILL.md at `~/.agents/skills/<name>/SKILL.md`.

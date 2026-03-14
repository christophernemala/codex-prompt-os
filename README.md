# codex-prompt-os

A private instruction system for GitHub Codex. This repo acts as a reusable control center for all development tasks across projects.

## Structure

```
codex-prompt-os/
├── AGENTS.md                  # Permanent Codex execution rules (loaded automatically)
├── prompts/
│   ├── dashboard.md           # Dashboard and data visualization tasks
│   ├── automation.md          # Script and pipeline automation tasks
│   ├── bugfix.md              # Bug investigation and fix tasks
│   ├── website.md             # UI and frontend tasks
│   ├── data-cleaning.md       # Data normalization and quality tasks
│   ├── finance-automation.md  # AR, O2C, reconciliation, and collections tasks
│   └── ai-agent.md            # LLM agent and tool-use tasks
├── templates/
│   ├── task-template.md       # Structured input format for new tasks
│   └── output-template.md     # Structured output format for completed work
└── README.md
```

## How to Use

### With Codex in VS Code
1. Open this repo (or add it as a worktree alongside your project repo)
2. Codex reads `AGENTS.md` automatically from the repo root
3. Copy the relevant prompt from `/prompts` for your task type
4. Paste your specific task at the bottom under `## Task`
5. Submit to Codex — it will follow the rules in `AGENTS.md` automatically

### Worktree Workflow
For parallel tasks without context mixing:
```bash
git worktree add ../task-feature-name -b feature/task-name
```
Each worktree gets its own isolated working directory.

### Adding a New Prompt
Copy `/templates/task-template.md`, fill in the details, and save it under `/prompts/your-task-type.md`.

## Why AGENTS.md

OpenAI Codex reads `AGENTS.md` at the repo root and uses it as persistent execution guidance. Encoding your standards here means you never have to re-explain your conventions, stack preferences, or output format for any task in any repo.

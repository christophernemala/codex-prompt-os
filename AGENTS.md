# AGENTS.md

You are working in this repository under strict execution rules.

## Core Behavior

- Do not ask the user unnecessary questions.
- Infer the most reasonable assumptions from repository files, filenames, folder names, existing code, comments, package files, and prior project structure.
- If something is missing, use the safest industry-standard default and continue.
- Only stop and ask a question if the task is impossible, destructive, or blocked by missing credentials, missing files, or conflicting requirements.
- Prefer action over discussion.
- Complete the task end to end.
- Preserve existing architecture unless the task explicitly requires refactoring.
- Keep all edits production-ready, clean, and minimal.
- Do not make unrelated changes.
- Before editing, inspect the repo and form a short plan internally.
- After editing, validate your work by checking affected files for consistency.
- When possible, run relevant linting, typecheck, or tests.
- If tests cannot run, explain exactly why in one sentence.
- Output concise status only:
  1. What changed
  2. Files changed
  3. Any blockers

## Execution Defaults

- Use existing stack and conventions in the repo.
- Reuse existing components and utilities before creating new ones.
- Keep naming consistent with the current codebase.
- Do not add dependencies unless necessary.
- If adding dependencies is required, choose stable, widely used packages.

## Task Handling

- Treat each new task as isolated from unrelated work.
- For parallel work, use separate worktrees or branches.
- Do not mix contexts across tasks.

## Output Format

After every task, return exactly this:

### Completed Work
[Brief summary of what was done]

### Files Changed
- `path/to/file.ext` — reason

### Blockers
[None, or describe blocker in one sentence]

# Claude-Style Assistant

A reusable, model-neutral working style for careful research, clear answers, and completed, verified work. Created for Christopher Nemala. Version 1.0.0.

This is an original adaptation of reusable practices from the user-supplied document and the agreed conversation draft. It is not an authenticated Anthropic system prompt, a model upgrade, or a verbatim archive of that document. Provider-specific internal tags, identity claims, runtime paths, and unavailable tools are excluded.

## Quick links

- [Read the skill](SKILL.md)
- [Portable yml.skill.md](yml.skill.md)
- [Raw URL for assistants](https://raw.githubusercontent.com/christophernemala/codex-prompt-os/main/skills/claude-style-assistant/yml.skill.md)
- [Preview and prompt harness](https://htmlpreview.github.io/?https://github.com/christophernemala/codex-prompt-os/blob/main/skills/claude-style-assistant/preview.html)
- [Harness source / download](preview.html)
- [Behavioral evaluation cases](evals.yaml)

The HTML preview uses the third-party HTMLPreview viewer. If it cannot load GitHub content, download preview.html and open it in a browser. GitHub's normal HTML file page displays source rather than running the harness.

## Included stack

| File | Purpose |
| --- | --- |
| SKILL.md | Standard skill entry point: YAML frontmatter plus Markdown |
| yml.skill.md | Identical portable copy under the requested filename |
| agents/openai.yaml | Codex-facing display metadata |
| README.md | Usage, installation, maintenance, and limitations |
| evals.yaml | Manual behavioral evaluation prompts and pass criteria |
| scripts/validate.py | Package consistency checks; Python 3 and PyYAML |
| preview.html | Self-contained prompt builder and manual checklist |

## Use from a URL

Paste this into an assistant that can fetch URLs:

> Read https://raw.githubusercontent.com/christophernemala/codex-prompt-os/main/skills/claude-style-assistant/yml.skill.md and apply its workflow guidance to the following task, within your existing permissions and available tools. If the URL cannot be fetched, tell me. Task: [describe the outcome, inputs, constraints, and completion criteria].

Reading a URL applies guidance to the current task. It does not install the skill, grant tools, or ensure persistence in other chats. If browsing is unavailable, attach SKILL.md or paste its contents.

The main-branch link follows updates. For reproducibility, replace main in the raw URL with the full Git commit SHA for the version reviewed.

## Claude Code installation

Create ~/.claude/skills/claude-style-assistant/ for personal use, or .claude/skills/claude-style-assistant/ inside a project. Put SKILL.md and any supporting files there. Invoke /claude-style-assistant.

Example on macOS/Linux, after reviewing the linked content:

```bash
mkdir -p ~/.claude/skills/claude-style-assistant
curl --fail --location 'https://raw.githubusercontent.com/christophernemala/codex-prompt-os/main/skills/claude-style-assistant/SKILL.md' \
  --output ~/.claude/skills/claude-style-assistant/SKILL.md
```

The single-file installation contains the full working guidance. Download the whole folder if you also need its maintenance tools and harness.

## Codex and ChatGPT

For Codex CLI, put the folder in your configured personal skills directory; the conventional default is ~/.codex/skills/claude-style-assistant/. Invoke $claude-style-assistant. Discovery and UI behavior depend on the host.

For this ChatGPT workspace, personal skill installation is handled separately from GitHub publication. In other chats or products, use their skill-import feature if available, or provide the raw URL or file. Do not assume every product loads arbitrary skill URLs automatically.

## Preview harness

Download preview.html and open it directly. It has no dependency installation, API key, backend, analytics, or model call.

1. Enter a task.
2. Generate a prompt containing the skill and task.
3. Copy or download the prompt and run it in your chosen assistant.
4. Use the checklist to review the response manually.

The checklist does not automatically grade model behavior. No prompt or response is submitted by the harness. The third-party hosted viewer may fetch the public HTML from GitHub.

## Validate and evaluate

Install PyYAML if needed, then run from this folder:

```bash
python3 -m pip install PyYAML
python3 scripts/validate.py
```

The validator checks frontmatter, identical skill copies, metadata, evaluation schema, and required package files. It does not prove an assistant will follow the instructions.

For behavioral evaluation, run each evals.yaml prompt in a fresh conversation with the skill loaded. Compare the response with every listed pass criterion and record pass, fail, or not tested. Keep tool availability consistent between comparisons. Never interpret an unchecked or unavailable case as passed.

## Updates

Edit SKILL.md, copy it to yml.skill.md, update the embedded preview text if the skill changes, run validation, and publish all changed files together. Keep the live raw URL for convenience and a commit-pinned URL for reproducibility.

## Boundaries

This package guides behavior. It does not replace the host's instruction hierarchy, provide hidden reasoning, bypass permissions, supply API credentials, execute autonomous schedules, or confer Claude's tools. The filename yml.skill.md is Markdown with YAML frontmatter; standard discovery still uses SKILL.md.

## Sources

- [Claude skills documentation](https://code.claude.com/docs/en/skills)
- [Agent Skills specification](https://agentskills.io/specification)
- The user-supplied Google Doc was consulted as unverified reference material. Its full text is not redistributed here.

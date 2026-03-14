# AI Agent Task Prompt

Complete this AI agent task end to end without asking questions unless execution is impossible due to missing credentials, missing required files, destructive risk, or contradictory instructions.

You must:
- Inspect the existing agent architecture: LLM provider, tool definitions, memory system, orchestration pattern
- Reuse existing tool wrappers and prompt templates before creating new ones
- Keep agent instructions deterministic and minimal to avoid hallucination
- Implement proper error handling for API failures, rate limits, and bad outputs
- Do not expose credentials or API keys in code
- Validate the agent flow end to end with a sample input before finalizing

Output only:
- Completed work
- Files changed
- Blockers

## Task

[PASTE AI AGENT TASK HERE]

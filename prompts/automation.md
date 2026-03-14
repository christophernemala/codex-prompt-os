# Automation Task Prompt

Complete this automation task end to end without asking questions unless execution is impossible due to missing credentials, missing required files, destructive risk, or contradictory instructions.

You must:
- Inspect the repository first
- Infer the automation framework, job scheduler, trigger mechanism, and data pipeline patterns
- Make reasonable assumptions about missing config and proceed
- Avoid creating new dependencies if existing utilities can handle the task
- Keep scripts idempotent where possible
- Handle errors and edge cases with appropriate logging
- Validate the automation logic end to end before finalizing

Output only:
- Completed work
- Files changed
- Blockers

## Task

[PASTE AUTOMATION TASK HERE]

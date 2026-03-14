# Bug Fix Task Prompt

Complete this bug fix end to end without asking questions unless execution is impossible due to missing credentials, missing required files, destructive risk, or contradictory instructions.

You must:
- Inspect the repository and reproduce the bug mentally from the code
- Identify the root cause before making any changes
- Fix only the root cause — do not patch symptoms
- Do not change unrelated code
- Reuse existing error handling patterns
- After fixing, validate that the bug is resolved and no regressions were introduced
- If a test exists for the affected area, verify it still passes

Output only:
- Root cause identified
- Fix applied
- Files changed
- Blockers

## Task

[PASTE BUG DESCRIPTION HERE]

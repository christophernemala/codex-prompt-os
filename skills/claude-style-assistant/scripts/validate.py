#!/usr/bin/env python3
"""Validate package structure; does not evaluate model behavior."""
from pathlib import Path
import json
import re
import yaml

root = Path(__file__).resolve().parents[1]
skill = (root / "SKILL.md").read_text()
match = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
assert match, "Missing YAML frontmatter"
meta = yaml.safe_load(match.group(1))
assert meta["name"] == "claude-style-assistant"
assert isinstance(meta["description"], str) and meta["description"].strip()
assert (root / "yml.skill.md").read_text() == skill, "Portable copy differs"
for name in ["README.md", "preview.html", "evals.yaml", "agents/openai.yaml"]:
    assert (root / name).is_file(), f"Missing {name}"
ui = yaml.safe_load((root / "agents/openai.yaml").read_text())
assert "$claude-style-assistant" in ui["interface"]["default_prompt"]
cases = yaml.safe_load((root / "evals.yaml").read_text())["cases"]
assert len({c["id"] for c in cases}) == len(cases)
assert all(c["prompt"] and c["pass_criteria"] for c in cases)
html = (root / "preview.html").read_text()
embedded = re.search(r'<script id="skill-data" type="application/json">(.*?)</script>', html, re.S)
assert embedded and json.loads(embedded.group(1)) == skill, "Preview skill differs"
print(f"PASS: package integrity; {len(cases)} manual cases available, not executed.")

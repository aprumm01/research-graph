"""
Builds notes-index.json from obsidian-vault for the vault-query frontend.
Run from graphify-out/ before pushing to research-graph.
"""
import json
import re
from pathlib import Path

VAULT = Path(__file__).parent / "obsidian-vault"
OUT = Path(__file__).parent / "notes-index.json"

SOURCE_FILE_RE = re.compile(r'source_file:\s*"(research_docs/P\d+\.pdf)"')

notes = []
for md in VAULT.rglob("*.md"):
    content = md.read_text(encoding="utf-8", errors="ignore")
    rel = md.relative_to(VAULT)
    entry: dict = {
        "path": str(rel).replace("\\", "/"),
        "title": md.stem,
        "content": content[:4000],  # cap per note to keep index reasonable
    }
    sf = SOURCE_FILE_RE.search(content)
    if sf:
        entry["source_file"] = sf.group(1)
    notes.append(entry)

OUT.write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")
print(f"Built {len(notes)} notes -> {OUT} ({OUT.stat().st_size // 1024}KB)")

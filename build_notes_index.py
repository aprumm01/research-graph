"""
Builds notes-index.json from obsidian-vault for the vault-query frontend.
Run from graphify-out/ before pushing to research-graph.
"""
import json
import re
from pathlib import Path

VAULT = Path(__file__).parent / "obsidian-vault"
OUT = Path(__file__).parent / "notes-index.json"
SNIPPETS_FILE = Path(__file__).parent / "paper-snippets.json"

SOURCE_FILE_RE = re.compile(r'source_file:\s*"(research_docs/P\d+\.pdf)"')
ABSTRACT_RE = re.compile(r'Abstract:\s*(.{40,}?)(?:\n\n|$)', re.DOTALL)

# Load snippets so we can add abstract text to the search index
snippets: dict = {}
if SNIPPETS_FILE.exists():
    snippets = json.loads(SNIPPETS_FILE.read_text(encoding="utf-8"))

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
        pid_m = re.search(r'P(\d+)\.pdf', sf.group(1))
        if pid_m:
            pid = f"P{pid_m.group(1)}"
            snippet = snippets.get(pid, "")
            abs_m = ABSTRACT_RE.search(snippet)
            if abs_m:
                # Include abstract in index for Fuse search — keeps index searchable
                # for stub notes that otherwise have no body text
                entry["abstract"] = abs_m.group(1).strip()[:500]

    notes.append(entry)

OUT.write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")
print(f"Built {len(notes)} notes -> {OUT} ({OUT.stat().st_size // 1024}KB)")

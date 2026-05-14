"""
build_paper_snippets.py
Builds paper-snippets.json: {PID: "abstract + methods excerpt", ...}

Reads .batch*.json (raw PDF text) + .graphify_semantic.json (PID→filename).
Only extracts Abstract and Methods sections — keeps snippets token-efficient
for use as additional context in vault-query.

Run from graphify-out/ before pushing to research-graph.
"""
import json
import re
from pathlib import Path

OUTDIR = Path(__file__).parent
OUT = OUTDIR / "paper-snippets.json"

ABSTRACT_RE = re.compile(
    r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*[:\-–—]?\s*\n([\s\S]+?)(?=\n\s*\n\s*(?:[A-Z][a-z]|\d[\.\s]|Keywords|CCS|ACM|Index\s+Terms)|$)',
    re.IGNORECASE,
)
ABSTRACT_INLINE_RE = re.compile(
    r'(?:Abstract|ABSTRACT)\s*[:\-–—\.]\s+([\s\S]{80,}?)(?=\n\n|\n[A-Z][a-z]+\s*\n|$)',
    re.IGNORECASE,
)
METHODS_RE = re.compile(
    r'\n\s*(?:\d+[\.\s]+)?(?:Method(?:s|ology)?|Study\s+Design|Research\s+Design|Procedure|Participants?\s+and\s+Method)\s*\n([\s\S]+?)(?=\n\s*(?:\d+[\.\s]+)?(?:Result|Finding|Discussion|Conclusion|Limitation|Implication))',
    re.IGNORECASE,
)


def extract_snippet(text: str) -> str:
    # Strip FILE: header
    text = re.sub(r"^FILE:[^\n]*\n", "", text).strip()

    parts = []

    # Abstract
    m = ABSTRACT_RE.search(text[:6000])
    if not m:
        m = ABSTRACT_INLINE_RE.search(text[:6000])
    if m:
        abstract = re.sub(r"\s+", " ", m.group(1).strip())[:600]
        parts.append(f"Abstract: {abstract}")

    # Methods
    m = METHODS_RE.search(text)
    if m:
        methods = re.sub(r"\s+", " ", m.group(1).strip())[:800]
        parts.append(f"Methods: {methods}")

    # Fallback if no sections found
    if not parts:
        fallback = re.sub(r"\s+", " ", text[:1400].strip())
        return fallback

    return "\n\n".join(parts)


def build_pid_to_origfile() -> dict[str, str]:
    sem = json.loads(
        (OUTDIR / ".graphify_semantic.json").read_text(encoding="utf-8", errors="replace")
    )
    return {
        node["id"]: node.get("properties", {}).get("original_file", "")
        for node in sem.get("nodes", [])
        if node.get("type") == "paper" and node.get("id")
    }


def build_batch_index() -> dict[str, str]:
    texts: dict[str, str] = {}
    for batch_file in sorted(OUTDIR.glob(".batch*.json")):
        batch = json.loads(batch_file.read_text(encoding="utf-8", errors="replace"))
        for key, text in batch.items():
            m = re.search(r"FILE:\s*(.+?)(?:\n|$)", text)
            fname = m.group(1).strip() if m else key.replace(".txt", "")
            texts[fname] = text
    return texts


def main() -> None:
    print("Loading PID -> original file mapping...")
    pid_to_orig = build_pid_to_origfile()

    print(f"Loading batch texts ({len(list(OUTDIR.glob('.batch*.json')))} files)...")
    batch_texts = build_batch_index()

    snippets: dict[str, str] = {}
    found = missing = 0

    for pid, orig_file in pid_to_orig.items():
        text = batch_texts.get(orig_file)

        if not text and orig_file:
            orig_stem = Path(orig_file).stem.lower()
            for fname, t in batch_texts.items():
                if Path(fname).stem.lower() == orig_stem:
                    text = t
                    break

        if text:
            snippets[pid] = extract_snippet(text)
            found += 1
        else:
            missing += 1

    OUT.write_text(json.dumps(snippets, ensure_ascii=False), encoding="utf-8")
    size_kb = OUT.stat().st_size // 1024
    print(f"Done: {found} snippets written, {missing} missing -> {OUT} ({size_kb} KB)")


if __name__ == "__main__":
    main()

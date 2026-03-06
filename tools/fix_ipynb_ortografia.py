#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import requests


LT_CHECK_URL = "https://api.languagetool.org/v2/check"
DEFAULT_LANGUAGE = "es"

# Ortho-ish corrections. Avoid style/grammar rewrites.
ALLOWED_ISSUE_TYPES = {"misspelling", "typographical", "whitespace"}

# MyST directives whose body is usually *not* prose.
CODELIKE_DIRECTIVES = {
    "code-block",
    "code-cell",
    "literalinclude",
    "math",
    "mermaid",
}


@dataclass(frozen=True)
class Segment:
    kind: str  # "plain" | "protected"
    text: str


def _is_generated_path(path: Path) -> bool:
    parts = {p.lower() for p in path.parts}
    if "_build" in parts:
        return True
    if ".ipynb_checkpoints" in parts:
        return True
    return False


def _loads_notebook(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _dumps_notebook(path: Path, nb: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
        f.write("\n")


def _cell_text(source: Any) -> Tuple[str, bool]:
    if isinstance(source, list):
        return "".join(source), True
    if isinstance(source, str):
        return source, False
    return str(source), False


def _set_cell_source(cell: Dict[str, Any], text: str, was_list: bool) -> None:
    if was_list:
        cell["source"] = text.splitlines(keepends=True)
    else:
        cell["source"] = text


_FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")


def _parse_directive_name(info: str) -> Optional[str]:
    info = info.strip()
    if not info.startswith("{"):
        return None
    end = info.find("}")
    if end == -1:
        return None
    inside = info[1:end].strip()
    if not inside:
        return None
    return inside.split()[0].strip()


def segment_markdown(text: str) -> List[Segment]:
    """Split markdown into segments safe to send to LanguageTool (plain) vs untouched (protected)."""
    out: List[Segment] = []
    lines = text.splitlines(keepends=True)
    i = 0
    outside_buf: List[str] = []

    def flush_outside() -> None:
        nonlocal outside_buf
        if outside_buf:
            out.extend(segment_inline("".join(outside_buf)))
            outside_buf = []

    while i < len(lines):
        line = lines[i]
        m = _FENCE_RE.match(line)
        if not m:
            outside_buf.append(line)
            i += 1
            continue

        flush_outside()

        fence = m.group(2)
        info = (m.group(3) or "").strip()
        directive = _parse_directive_name(info)

        j = i + 1
        while j < len(lines):
            close_line = lines[j]
            if close_line.lstrip().startswith(fence) and close_line.strip().strip("`~") == "":
                break
            j += 1

        if j >= len(lines):
            out.append(Segment("protected", "".join(lines[i:])))
            return out

        block_lines = lines[i : j + 1]

        if directive is None or directive in CODELIKE_DIRECTIVES:
            out.append(Segment("protected", "".join(block_lines)))
        else:
            out.append(Segment("protected", lines[i]))
            body = "".join(lines[i + 1 : j])
            if body:
                out.extend(segment_inline(body))
            out.append(Segment("protected", lines[j]))

        i = j + 1

    flush_outside()
    return out


def segment_inline(text: str) -> List[Segment]:
    """Inline segmentation on non-fenced markdown."""
    segments: List[Segment] = []

    def push(kind: str, s: str) -> None:
        if not s:
            return
        if segments and segments[-1].kind == kind:
            segments[-1] = Segment(kind, segments[-1].text + s)
        else:
            segments.append(Segment(kind, s))

    i = 0
    n = len(text)
    while i < n:
        ch = text[i]

        # Inline code spans: `...` (support multiple backticks).
        if ch == "`":
            run = 1
            while i + run < n and text[i + run] == "`":
                run += 1
            close = text.find("`" * run, i + run)
            if close != -1:
                push("plain", text[:i])
                push("protected", text[i : close + run])
                text = text[close + run :]
                n = len(text)
                i = 0
                continue

        # Math: $...$ or $$...$$
        if ch == "$" and (i == 0 or text[i - 1] != "\\"):
            run = 2 if (i + 1 < n and text[i + 1] == "$") else 1
            token = "$" * run
            close = text.find(token, i + run)
            if close != -1:
                push("plain", text[:i])
                push("protected", text[i : close + run])
                text = text[close + run :]
                n = len(text)
                i = 0
                continue

        # Link URL targets: ](url)
        if ch == "(" and i >= 1 and text[i - 1] == "]":
            j = i + 1
            while j < n:
                if text[j] == ")" and text[j - 1] != "\\":
                    break
                j += 1
            if j < n:
                push("plain", text[:i])
                push("protected", text[i : j + 1])
                text = text[j + 1 :]
                n = len(text)
                i = 0
                continue

        i += 1

    push("plain", text)
    return segments


def _needs_check(text: str) -> bool:
    return bool(re.search(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", text))


def lt_check(text: str, language: str, session: requests.Session) -> Dict[str, Any]:
    r = session.post(
        LT_CHECK_URL,
        data={
            "text": text,
            "language": language,
        },
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def apply_lt_orthography(text: str, language: str, session: requests.Session, cache: Dict[str, str]) -> str:
    if not _needs_check(text):
        return text
    cached = cache.get(text)
    if cached is not None:
        return cached

    data = lt_check(text, language, session)
    matches = data.get("matches", []) or []

    edits: List[Tuple[int, int, str]] = []
    for m in matches:
        rule = m.get("rule", {}) or {}
        issue_type = rule.get("issueType") or m.get("ruleIssueType")
        if issue_type not in ALLOWED_ISSUE_TYPES:
            continue
        reps = m.get("replacements", []) or []
        if not reps:
            continue
        replacement = reps[0].get("value")
        if not replacement:
            continue
        offset = int(m.get("offset", 0))
        length = int(m.get("length", 0))
        if length <= 0:
            continue
        edits.append((offset, offset + length, replacement))

    edits.sort(key=lambda e: e[0], reverse=True)
    out = text
    for start, end, repl in edits:
        if start < 0 or end > len(out) or start >= end:
            continue
        out = out[:start] + repl + out[end:]

    cache[text] = out
    return out


def correct_markdown(text: str, language: str, session: requests.Session, cache: Dict[str, str]) -> str:
    pieces = segment_markdown(text)
    corrected: List[str] = []
    for seg in pieces:
        if seg.kind == "protected":
            corrected.append(seg.text)
        else:
            corrected.append(apply_lt_orthography(seg.text, language, session, cache))
    return "".join(corrected)


def iter_ipynb_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.ipynb"):
        if _is_generated_path(path):
            continue
        yield path


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Corrige ortografía en celdas Markdown/Raw de notebooks .ipynb.")
    parser.add_argument("--root", default=".", help="Directorio raíz (por defecto: .)")
    parser.add_argument("--language", default=DEFAULT_LANGUAGE, help="Código de idioma (por defecto: es)")
    parser.add_argument("--limit", type=int, default=0, help="Limitar notebooks (0 = sin límite)")
    parser.add_argument("--dry-run", action="store_true", help="No escribe cambios; solo reporta.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    language = args.language

    paths = list(iter_ipynb_files(root))
    if args.limit and args.limit > 0:
        paths = paths[: args.limit]

    session = requests.Session()
    session.headers.update({"User-Agent": "ipynb-ortografia-fix/1.0 (educational; LanguageTool public API)"})
    cache: Dict[str, str] = {}

    changed_files = 0
    changed_cells = 0

    for path in paths:
        nb = _loads_notebook(path)
        cells = nb.get("cells", []) or []
        file_changed = False

        for cell in cells:
            if not isinstance(cell, dict):
                continue
            if cell.get("cell_type") not in {"markdown", "raw"}:
                continue
            source = cell.get("source", "")
            text, was_list = _cell_text(source)
            new_text = correct_markdown(text, language, session, cache)
            if new_text != text:
                file_changed = True
                changed_cells += 1
                _set_cell_source(cell, new_text, was_list)

        if file_changed:
            changed_files += 1
            if not args.dry_run:
                _dumps_notebook(path, nb)
            print(f"UPDATED {path}")

    print(f"Done. Notebooks scanned: {len(paths)}. Updated: {changed_files}. Cells changed: {changed_cells}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Autochecagem automática dos prompts (SKILL.md §12.1, itens 2, 4 e 5).

Uso:
    python lint_prompts.py prompts/slide-*.txt

Linhas que começam com "#" são notas (ex.: "# slide 3 · MK06 · L8"): não vão
ao gerador e são onde o movimento MK de cada prompt deve ser registrado.
"""

import argparse
import math
import re
import sys
from pathlib import Path

BANNED = re.compile(r"cerulean|grassy hill|35mm f/2 at eye level|\bidentity\b|same face|"
                    r"match the reference (?:image )?exactly", re.IGNORECASE)
MOVEMENT = re.compile(r"\b(?:MK\d{2}|IG\d{2}|R\d{2}|N\d{2}|TM\d)\b")
TEXT_BLOCK = re.compile(r"^\s*(?:Text(?:,\s*rendered exactly)?|Render exactly)\s*:", re.IGNORECASE | re.MULTILINE)
GLOBAL_TEXT_BAN = re.compile(
    r"^\s*(?:do not include|don't include|do not render|no)\s+(?:any\s+)?text(?=\s*[,.;:]|\s*$)"
    r"|^\s*(?:não incluir|nao incluir|sem)\s+(?:qualquer\s+)?texto(?=\s*[,.;:]|\s*$)",
    re.IGNORECASE | re.MULTILINE)
UNFILLED = re.compile(r"\{[^{}\n]+\}|\[[^\[\]\n]+\]")
QUOTED_TEXT = re.compile(r'["“]([^"”]+)["”]')
TEXT_EXCEPTION = re.compile(
    r"\b(?:other than|except|beyond)\b.*\b(?:listed|specified|authorized)\b"
    r"|(?:além|alem|exceto)\b.*\b(?:listado|especificado|autorizado)",
    re.IGNORECASE)


def copy_errors(body: str, background_only: bool) -> list[str]:
    errors = []
    text_block = TEXT_BLOCK.search(body)
    copy = body[text_block.end():] if text_block else ""
    copy = re.split(r"^\s*Render only the exact text", copy, maxsplit=1,
                    flags=re.IGNORECASE | re.MULTILINE)[0]
    has_copy = any(match.group(1).strip() for match in QUOTED_TEXT.finditer(copy))
    if not background_only and not has_copy:
        errors.append("texto exato ausente ou vazio; incluir a lista literal ou pedir --background-only")
    for line in body.splitlines():
        if has_copy and GLOBAL_TEXT_BAN.search(line) and not TEXT_EXCEPTION.search(line):
            errors.append("conflito: lista de texto junto de proibição global de texto")
            break
    if UNFILLED.search(body):
        errors.append("campos por preencher no prompt final")
    return errors


def split_prompt(text: str) -> tuple[list[str], str]:
    notes = [line for line in text.splitlines() if line.lstrip().startswith("#")]
    body = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#")).strip()
    return notes, body


def camera_line(body: str) -> str | None:
    match = re.search(r"^\s*Camera:\s*(.+)$", body, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip().lower() if match else None


def lint_prompt(text: str, background_only: bool = False) -> dict:
    notes, body = split_prompt(text)
    return {
        "banned": sorted({m.group(0) for m in BANNED.finditer(body)}),
        "camera": camera_line(body),
        "movement": bool(MOVEMENT.search(" ".join(notes))),
        "copy_errors": copy_errors(body, background_only),
    }


def lint_series(paths: list[Path], background_only: bool = False) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    cameras = []
    for path in paths:
        result = lint_prompt(path.read_text(encoding="utf-8"), background_only)
        if result["banned"]:
            errors.append(f"{path.name}: termos proibidos no prompt: {', '.join(result['banned'])}")
        errors.extend(f"{path.name}: {error}" for error in result["copy_errors"])
        if result["camera"] is None:
            warnings.append(f"{path.name}: sem linha 'Camera:' (a câmera vem do storyboard)")
        else:
            cameras.append(result["camera"])
        if not result["movement"]:
            warnings.append(f"{path.name}: sem nota '# ... MK##' com o movimento de origem")
    if len(paths) > 1:
        needed = math.ceil(len(paths) / 2)
        distinct = len(set(cameras))
        if distinct < needed:
            errors.append(f"série: {distinct} câmeras distintas em {len(paths)} prompts; mínimo {needed}")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("prompts", nargs="+", type=Path)
    parser.add_argument("--background-only", action="store_true",
                        help="Apenas fundo/foto, quando solicitado explicitamente; dispensa copy.")
    args = parser.parse_args()
    errors, warnings = lint_series(args.prompts, args.background_only)
    for line in warnings:
        print("AVISO " + line)
    for line in errors:
        print("ERRO " + line)
    print(f"AUTOCHECAGEM {'REPROVADA' if errors else 'OK'}: {len(args.prompts)} prompt(s), "
          f"{len(errors)} erro(s), {len(warnings)} aviso(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
# ]
# ///
"""Gera imagens com Gemini 3 Pro Image em proporcao nativa, com referencias opcionais.

Uso (python ou uv run):
    python generate.py --prompt-file prompt.txt --out hero-desktop.png --aspect 16:9 --size 2K
    python generate.py --prompt-file mobile.txt --out hero-mobile.png --aspect 9:16 --ref hero-desktop.png
    python generate.py --prompt-file slide-01.txt --out teste.png --aspect 4:5 --dry-run

Linhas do arquivo que começam com "#" são notas e não vão ao gerador. O --dry-run
confere acervo, argumentos, referências e termos proibidos sem importar o SDK.

A chave vem somente de GEMINI_API_KEY, para nao ficar no historico do shell.
"""

import argparse
import json
import os
import sys
from io import BytesIO
from pathlib import Path

from check_assets import check_assets
from lint_prompts import lint_prompt, split_prompt

ASPECTS = ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]
SIZES = ["1K", "2K", "4K"]
DEFAULT_MODEL = "gemini-3-pro-image-preview"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gera imagem em proporcao nativa (Gemini 3 Pro Image)."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--prompt", help="Prompt em linha.")
    source.add_argument("--prompt-file", type=Path, help="Arquivo UTF-8 com o prompt.")
    parser.add_argument("--out", required=True, type=Path, help="Arquivo PNG de saida.")
    parser.add_argument("--aspect", required=True, choices=ASPECTS, help="Proporcao nativa.")
    parser.add_argument("--size", default="2K", choices=SIZES, help="Resolucao (padrao 2K).")
    parser.add_argument(
        "--ref",
        action="append",
        default=[],
        type=Path,
        help="Imagem de referencia (repetivel): master aprovado, slide anterior, recorte.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Modelo de imagem.")
    parser.add_argument(
        "--cliente",
        help="Incluir clientes/<nome> na checagem do acervo (so quando o usuario nomeia o cliente).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Valida entradas e mostra a requisicao sem chamar a API.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    acervo = check_assets(Path(__file__).resolve().parents[1], args.cliente)
    if acervo["erros"]:
        sys.exit("Erro no acervo; geração bloqueada:\n" + "\n".join(acervo["erros"]))

    raw = args.prompt if args.prompt is not None else args.prompt_file.read_text(encoding="utf-8")
    # Linhas iniciadas por "#" são notas do storyboard (movimento MK etc.): nunca vão ao gerador.
    notes, prompt = split_prompt(raw)
    if not prompt:
        sys.exit("Erro: prompt vazio.")
    if args.out.suffix.lower() != ".png":
        sys.exit("Erro: --out deve terminar em .png.")
    for ref in args.ref:
        if not ref.is_file():
            sys.exit(f"Erro: referencia nao encontrada: {ref}")

    lint = lint_prompt(raw)
    if lint["banned"]:
        sys.exit("Erro: termos proibidos no prompt (SKILL.md §12.1): " + ", ".join(lint["banned"]))

    if args.dry_run:
        print(
            json.dumps(
                {
                    "model": args.model,
                    "out": str(args.out),
                    "refs": [str(ref) for ref in args.ref],
                    "image_config": {"aspect_ratio": args.aspect, "image_size": args.size},
                    "prompt_chars": len(prompt),
                    "notas_removidas": len(notes),
                    "camera": lint["camera"] or "AVISO: sem linha Camera:",
                    "movimento_registrado": lint["movement"],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    from google.genai import types

    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio=args.aspect, image_size=args.size),
    )

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Erro: defina a variavel de ambiente GEMINI_API_KEY.")

    from google import genai
    from PIL import Image

    references = [Image.open(ref) for ref in args.ref]
    client = genai.Client(api_key=api_key)
    print(f"Gerando {args.aspect} {args.size} com {len(references)} referencia(s)...")
    response = client.models.generate_content(
        model=args.model,
        contents=[*references, prompt],
        config=config,
    )

    for part in response.parts or []:
        if part.text:
            print(f"Modelo: {part.text}")
        elif part.inline_data is not None:
            data = part.inline_data.data
            if isinstance(data, str):
                import base64

                data = base64.b64decode(data)
            image = Image.open(BytesIO(data))
            args.out.parent.mkdir(parents=True, exist_ok=True)
            image.save(args.out, "PNG")
            print(f"Salvo: {args.out.resolve()} ({image.width}x{image.height})")
            return

    sys.exit("Erro: o modelo nao retornou imagem (possivel bloqueio de seguranca ou cota).")


if __name__ == "__main__":
    main()

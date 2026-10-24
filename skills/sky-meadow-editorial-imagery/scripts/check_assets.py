#!/usr/bin/env python3
"""Confere o catálogo antes de consultar imagens ou gerar uma peça (sem rede)."""

import argparse
import hashlib
import json
from pathlib import Path


def check_assets(root: Path) -> dict:
    root = root.resolve()
    report = {"raiz": str(root), "verificados": [], "indisponiveis": [], "erros": []}
    try:
        catalog = json.loads((root / "assets/catalogo.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        report["erros"].append(f"Catálogo ilegível: {exc}")
        return report

    def check_file(label, relative, expected_hash=None, expected_bytes=None):
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            report["erros"].append(f"{label}: caminho fora da skill: {relative}")
            return
        try:
            with path.open("rb") as source:
                hasher = hashlib.sha256()
                for chunk in iter(lambda: source.read(1024 * 1024), b""):
                    hasher.update(chunk)
                digest = hasher.hexdigest()
            if expected_hash is not None and digest != expected_hash:
                report["erros"].append(f"{label}: SHA256 divergente: {relative}")
                return
            if expected_bytes is not None and path.stat().st_size != expected_bytes:
                report["erros"].append(f"{label}: tamanho divergente: {relative}")
                return
        except OSError as exc:
            report["erros"].append(f"{label}: arquivo ausente ou ilegível: {relative} ({exc})")
            return
        report["verificados"].append({"id": label, "caminho": relative, "sha256": digest})

    for item in catalog.get("itens", []) + catalog.get("derivados", []):
        label = item["id"]
        if not item.get("caminho"):
            if item.get("distribuido"):
                report["erros"].append(f"{label}: distribuído mas sem caminho no catálogo")
            else:
                report["indisponiveis"].append(label)
            continue
        if not item.get("sha256"):
            report["erros"].append(f"{label}: SHA256 ausente no catálogo")
            continue
        check_file(label, item["caminho"], item["sha256"], item.get("bytes"))
        thumbnail = item.get("miniatura")
        if thumbnail and thumbnail.get("caminho"):
            check_file(label + "/miniatura", thumbnail["caminho"],
                       thumbnail.get("sha256"), thumbnail.get("bytes"))
    for index in catalog.get("indices", []):
        check_file("índice", index)
    report["nao_recuperado"] = catalog.get("nao_recuperado", [])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Raiz da skill (padrão: instalação deste script).")
    parser.add_argument("--json", action="store_true", help="Relatório estruturado.")
    args = parser.parse_args()
    report = check_assets(args.root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"ACERVO {'ERRO' if report['erros'] else 'OK'}: "
              f"{len(report['verificados'])} arquivos lidos (hash comparado quando catalogado); "
              f"{len(report['indisponiveis'])} itens não distribuídos nesta instalação.")
        print(f"Raiz: {report['raiz']}")
        for entry in report["verificados"]:
            print(f"OK {entry['id']}: {entry['caminho']}")
        if report["indisponiveis"]:
            print("Sem pixels nesta instalação: " + ", ".join(report["indisponiveis"]))
        for item in report.get("nao_recuperado", []):
            print("Não recuperado (registro histórico): " + item["descricao"])
        for error in report["erros"]:
            print("ERRO " + error)
    return 1 if report["erros"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

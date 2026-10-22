#!/usr/bin/env python3
"""
render.py - turn a carousel HTML deck into numbered PNG slides, or dump the
slide text for the humanizer.

The deck is one HTML file with one <section class="slide"> per slide, each
1080x1350 (Instagram 4:5). Every section is screenshotted on its own, so the
PNG is exactly the slide, nothing around it.

Usage
  python render.py deck.html --out slides/        # slides/slide-01.png ...
  python render.py deck.html --text deck.txt      # visible text, one block per slide
  python render.py deck.html --out slides/ --scale 2   # 2160x2700 export

Needs Playwright (pip install playwright). Uses Playwright's Chromium when it
is installed, otherwise the system Chrome or Edge.
"""

import argparse
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

WIDTH, HEIGHT = 1080, 1350


def launch(p):
    errors = []
    for kwargs in ({}, {"channel": "chrome"}, {"channel": "msedge"}):
        try:
            return p.chromium.launch(**kwargs)
        except Exception as exc:  # browser not installed under that channel
            errors.append(f"{kwargs or 'bundled'}: {str(exc).splitlines()[0]}")
    sys.exit("no Chromium found. Run `python -m playwright install chromium`.\n  "
             + "\n  ".join(errors))


def main():
    ap = argparse.ArgumentParser(description="Render a carousel deck to PNG slides.")
    ap.add_argument("deck", help="HTML file with <section class=\"slide\"> per slide")
    ap.add_argument("--out", help="directory for slide-NN.png")
    ap.add_argument("--text", help="write the visible text of every slide here")
    ap.add_argument("--scale", type=float, default=1.0, help="device scale factor")
    args = ap.parse_args()
    if not (args.out or args.text):
        ap.error("pass --out, --text, or both")

    deck = Path(args.deck).resolve()
    with sync_playwright() as p:
        browser = launch(p)
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT},
                                device_scale_factor=args.scale)
        page.goto(deck.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        slides = page.locator("section.slide")
        count = slides.count()
        if not count:
            sys.exit(f"{deck.name}: no <section class=\"slide\"> found")
        if not 2 <= count <= 20:
            print(f"warning: {count} slides; Instagram accepts 2 to 20", file=sys.stderr)

        for i in range(count):
            slide = slides.nth(i)
            box = slide.bounding_box()
            if (round(box["width"]), round(box["height"])) != (WIDTH, HEIGHT):
                print(f"warning: slide {i + 1} is {box['width']:.0f}x{box['height']:.0f}, "
                      f"expected {WIDTH}x{HEIGHT}", file=sys.stderr)
            overflow = slide.evaluate(
                "el => [el, ...el.querySelectorAll('*')].some(c =>"
                " getComputedStyle(c).overflow !== 'visible' &&"
                " (c.scrollHeight > c.clientHeight + 1 || c.scrollWidth > c.clientWidth + 1))")
            if overflow:
                print(f"warning: slide {i + 1} has clipped text", file=sys.stderr)
            if args.out:
                os.makedirs(args.out, exist_ok=True)
                target = Path(args.out) / f"slide-{i + 1:02d}.png"
                slide.screenshot(path=str(target))
                print(target)

        # The copy the humanizer should read: no counters, icons or other
        # elements marked aria-hidden="true".
        page.add_style_tag(content="[aria-hidden='true'] { display: none !important; }")
        blocks = [f"[{i + 1}]\n" + slides.nth(i).inner_text().strip() for i in range(count)]
        browser.close()

    if args.text:
        Path(args.text).write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
        print(f"wrote {args.text}", file=sys.stderr)


if __name__ == "__main__":
    main()

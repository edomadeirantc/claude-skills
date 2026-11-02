"""Contratos de prompt completo e navegação editorial, sem chamadas de API."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
COMPLETE = '''# slide 1 · MK22 organizar · L8
A portrait 4:5 editorial carousel cover for a fictional scheduling guide.
Camera: 50mm lens, tabletop height, oblique angle.
A translucent appointment tile fits into a printed schedule; cream, black and coral.
Text, rendered exactly:
- "@agenda.demo" centered at 50% width, baseline at 6% height.
- "SUA AGENDA TEM VAZIOS?" at 8% width, 20% height, large condensed sans.
- "Comece pela confirmação." below the headline, readable sans.
Render only the exact text listed above; no additional lettering.
'''
BACKGROUND = '''# slide 1 · MK22 organizar · L8
A portrait 4:5 photograph of a scheduling tile on a real counter.
Camera: 50mm lens, tabletop height, oblique angle.
Do not include any text, letters or numbers.
'''


class PromptContractTests(unittest.TestCase):
    def lint(self, text, *flags):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "slide.txt"
            path.write_text(text, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPTS / "lint_prompts.py"),
                                   *flags, str(path)], capture_output=True, text=True,
                                  encoding="utf-8")

    def test_missing_copy_is_rejected_for_a_complete_artwork(self):
        result = self.lint(BACKGROUND)
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_text_list_conflicting_with_a_global_text_ban_is_rejected(self):
        result = self.lint(COMPLETE + "Do not include any text, letters or numbers.\n")
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_explicit_background_mode_does_not_require_copy(self):
        result = self.lint(BACKGROUND, "--background-only")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_filled_copy_is_accepted_but_an_unresolved_headline_is_rejected(self):
        self.assertEqual(self.lint(COMPLETE).returncode, 0)
        result = self.lint(COMPLETE.replace("SUA AGENDA TEM VAZIOS?", "{TÍTULO}"))
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_empty_footer_does_not_cancel_copy_elsewhere(self):
        result = self.lint(COMPLETE + "Keep the footer empty, with no text inside that band.\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_canonical_square_bracket_fields_are_rejected(self):
        result = self.lint(COMPLETE.replace("SUA AGENDA TEM VAZIOS?", "[título preenchido, quebras e posição]"))
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_empty_text_block_cannot_replace_actual_copy(self):
        result = self.lint("Camera: overhead.\nText, rendered exactly:\n")
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_closed_text_list_is_not_a_global_text_ban(self):
        result = self.lint(COMPLETE + "Do not include any text, letters or numbers other than those listed above.\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_dry_run_enforces_copy_without_calling_the_image_api(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = [sys.executable, str(SCRIPTS / "generate.py"), "--prompt", BACKGROUND,
                    "--out", str(Path(tmp) / "background.png"), "--aspect", "4:5", "--dry-run"]
            rejected = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
            self.assertNotEqual(rejected.returncode, 0)
            accepted = subprocess.run([*args, "--background-only"], capture_output=True,
                                      text=True, encoding="utf-8")
            self.assertEqual(accepted.returncode, 0, accepted.stdout + accepted.stderr)
            self.assertEqual(json.loads(accepted.stdout)["image_config"]["aspect_ratio"], "4:5")
            self.assertFalse((Path(tmp) / "background.png").exists())


class EditorialNavigationTests(unittest.TestCase):
    def test_progress_tracks_current_page_without_repeated_page_markers(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(["node", str(SCRIPTS / "kit_overlay.mjs"),
                                     "--total", "8", "--out", tmp], capture_output=True,
                                    text=True, encoding="utf-8")
            self.assertEqual(result.returncode, 0, result.stderr)
            ns = {"s": "http://www.w3.org/2000/svg"}
            slide = ET.parse(Path(tmp) / "kit-03.svg").getroot()
            labels = ["".join(node.itertext()) for node in slide.findall("s:text", ns)]
            fractions = [tuple(map(int, label.split("/"))) for label in labels if "/" in label]
            self.assertIn((3, 8), fractions)
            self.assertEqual(slide.findall("s:polygon", ns), [])
            self.assertEqual(slide.findall("s:circle", ns), [])
            self.assertEqual(slide.findall("s:rect", ns), [])
            lines = slide.findall("s:line", ns)
            self.assertEqual(len(lines), 2, "Uma trilha e um preenchimento, não um marcador por página")
            widths = [float(node.attrib["x2"]) - float(node.attrib["x1"]) for node in lines]
            self.assertAlmostEqual(widths[1] / widths[0], 3 / 8, places=2)
            last = ET.parse(Path(tmp) / "kit-08.svg").getroot()
            final_labels = ["".join(node.itertext()) for node in last.findall("s:text", ns)]
            final_fractions = [tuple(map(int, label.split("/"))) for label in final_labels if "/" in label]
            self.assertIn((8, 8), final_fractions)
            self.assertFalse(any("ARRASTE" in label for label in final_labels))


if __name__ == "__main__":
    unittest.main()

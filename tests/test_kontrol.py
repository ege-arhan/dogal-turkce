import io
import json
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import kontrol  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
KALIPLAR = ROOT / "references" / "kaliplar.json"
KALIPLAR_MD = ROOT / "references" / "kaliplar.md"


class KontrolUnitTests(unittest.TestCase):
    def test_tr_lower_length(self):
        s = "İSTANBUL ve Işık"
        out = kontrol.tr_lower(s)
        self.assertEqual(len(out), len(s))
        self.assertIn("ı", out)

    def test_strip_code_preserves_length(self):
        text = "Önce `kod` sonra https://x.test/y son."
        out = kontrol.strip_code(text)
        self.assertEqual(len(out), len(text))
        self.assertNotIn("`", out.replace(" ", ""))

    def test_scan_c1(self):
        text = "Harika bir soru! Uyku düzeni önemli."
        hits = kontrol.scan(text, genre="chat")
        ids = {h["id"] for h in hits}
        self.assertIn("C1", ids)

    def test_scan_b2_overlapping_patterns_one_hit(self):
        text = "- **Kafein:** öğleden sonra kes."
        b2 = [h for h in kontrol.scan(text) if h["id"] == "B2"]
        self.assertEqual(len(b2), 1)

    def test_scan_t7_muaf_formal(self):
        text = "Toplantı yapılmaktadır."
        chat = kontrol.scan(text, genre="chat")
        formal = kontrol.scan(text, genre="formal")
        self.assertTrue(any(h["id"] == "T7" for h in chat))
        self.assertFalse(any(h["id"] == "T7" for h in formal))

    def test_density_math(self):
        patterns, weights = kontrol.load_patterns(KALIPLAR)
        text = "Harika bir soru! " * 3
        d = kontrol.density(text, genre="chat", patterns=patterns, weights=weights)
        self.assertGreater(d, 0.0)

    def test_protected_diff_placeholder(self):
        self.assertIn("placeholder", kontrol.protected_diff("[not]", "metin", []))

    def test_protected_diff_url_period(self):
        self.assertEqual(
            kontrol.protected_diff("bk. https://a.test", "bk. https://a.test.", []),
            [],
        )

    def test_kaliplar_loads(self):
        patterns, _ = kontrol.load_patterns(KALIPLAR)
        self.assertGreater(len(patterns), 20)

    @unittest.skipUnless(KALIPLAR_MD.is_file(), "references/kaliplar.md missing")
    def test_ids_in_md(self):
        patterns, _ = kontrol.load_patterns(KALIPLAR)
        md = KALIPLAR_MD.read_text(encoding="utf-8")
        for pat in patterns:
            self.assertIn(pat["id"], md)


class KontrolCliTests(unittest.TestCase):
    def run_kontrol(self, argv):
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS / "kontrol.py")] + argv,
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        return proc

    def test_karsilastir_exit_on_number_change(self):
        src = ROOT / ".local" / "_kontrol_src.txt"
        out = ROOT / ".local" / "_kontrol_out.txt"
        src.parent.mkdir(parents=True, exist_ok=True)
        src.write_text("3 elma", encoding="utf-8")
        out.write_text("2 elma", encoding="utf-8")
        proc = self.run_kontrol(["karsilastir", str(src), str(out)])
        self.assertEqual(proc.returncode, 1)


if __name__ == "__main__":
    unittest.main()

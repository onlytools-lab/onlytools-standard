import json
import tempfile
import os
import unittest
from pathlib import Path
from scripts.check_product_version import check

class ProductVersionTests(unittest.TestCase):
    def test_json_and_msbuild(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            a = base / "package.json"
            b = base / "app.csproj"
            a.write_text(json.dumps({"version": "0.1.4-alpha.1"}))
            b.write_text("<Project><PropertyGroup><Version>0.1.4-alpha.1</Version></PropertyGroup></Project>")
            previous = os.getcwd()
            try:
                os.chdir(base)
                self.assertTrue(check("0.1.4-alpha.1", ["package.json", "app.csproj"]))
                with self.assertRaises(ValueError):
                    check("0.1.5", ["package.json", "app.csproj"])
            finally:
                os.chdir(previous)
    def test_missing_file_fails(self):
        with self.assertRaises(ValueError):
            check("1.0.0", ["missing.csproj"])

if __name__ == "__main__":
    unittest.main()

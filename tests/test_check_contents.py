from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ContentsInventoryTests(unittest.TestCase):
    def test_generated_contents_inventory_is_current(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/check_contents.py", "--check"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)


if __name__ == "__main__":
    unittest.main()

"""Smoke test verifying package import and fundamental properties."""

import unittest


class TestSmoke(unittest.TestCase):
    def test_package_metadata(self):
        import rag_evals

        self.assertTrue(hasattr(rag_evals, "__version__"))
        self.assertEqual(rag_evals.__version__, "0.1.0")
        self.assertTrue(hasattr(rag_evals, "AppConfig"))
        self.assertTrue(hasattr(rag_evals, "load_config"))


if __name__ == "__main__":
    unittest.main()

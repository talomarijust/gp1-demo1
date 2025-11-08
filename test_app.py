import unittest
from app import add_numbers

class TestMath(unittest.TestCase):
    def test_addition_correct(self):
        self.assertEqual(add_numbers(2, 3), 5)  # ✅ Pass

    def test_addition_fail(self):
        self.assertEqual(add_numbers(2, 3), 6)  # ❌ Fail (for demo)

if __name__ == "__main__":
    unittest.main()

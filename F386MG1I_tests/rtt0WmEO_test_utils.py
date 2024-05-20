# Tests for utils.py
import unittest
from module.utils import add

class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

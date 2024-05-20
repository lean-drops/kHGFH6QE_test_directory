# Tests for helpers.py
import unittest
from module.helpers import greet

class TestHelpers(unittest.TestCase):
    def test_greet(self):
        # Capture the output of the greet function
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        greet('Test')
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), 'Hello, Test!')

if __name__ == '__main__':
    unittest.main()

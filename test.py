from max import max_element
from max import min_element
import unittest

class TestMax(unittest.TestCase):
    def test_Max(self):
        actual = max_element([1,4,5])
        self.assertEqual(actual,5)

    def test_min(self):
        self.assertEqual(
            min_element([1,4,5]), 1)

if __name__ == '__main__':
    unittest.main()
from .context import *

import unittest

class SwapTestSuite(unittest.TestCase):
    """Swap Operation Test Case"""
    def setUp(self):
        self.a = 1
        self.b = 2

    def test_swap_operations(self):
        instance = Swap(self.a,self.b)
        value1, value2 =instance.get_swap_values()
        self.assertEqual(self.a, value2)
        self.assertEqual(self.b, value1)

if __name__ == '__main__':
    unittest.main()

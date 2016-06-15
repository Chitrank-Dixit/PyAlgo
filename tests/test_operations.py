from .context import *

import unittest

class SwapTestSuite(unittest.TestCase):
    """Swap Operation Test Case"""

    def test_items_swapped(self):
        a = 1
        b = 2
        instance = Swap(a,b)
        value1, value2 =instance.get_swap_values()
        self.assertEqual(a, value2)
        self.assertEqual(b, value1)


if __name__ == '__main__':
    unittest.main()

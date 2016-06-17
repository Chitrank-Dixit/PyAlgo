from .context import *

import unittest

class LinearSearchTestSuite(unittest.TestCase):
    """Linear Operation Test Case"""
    def setUp(self):
        self.input_list = [12,34,23,56,45,67]

    def test_linear_search(self):
        instance = LinearSearch(self.input_list)
        index = instance.search_item(23)
        self.assertEqual(self.input_list.index(23), index)

if __name__ == '__main__':
    unittest.main()

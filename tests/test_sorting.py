from .context import *

import unittest

class InsertionSortTestSuite(unittest.TestCase):
    """Insertion Sort Test Case"""
    def setUp(self):
        self.input_list = [12, 65, 23, 67, 45, 78, 90, 34, 23, 67, 45]

    def test_insertion_sort(self):
        instance = InsertionSort(self.input_list)
        output_list = instance.sort()
        self.assertEqual(sorted(self.input_list), output_list)

        output_list = instance.sort(reverse=True)
        self.assertEqual(sorted(self.input_list, reverse=True), output_list)


if __name__ == '__main__':
    unittest.main()


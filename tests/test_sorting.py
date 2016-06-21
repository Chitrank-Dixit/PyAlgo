from .context import *

import unittest


class SortingInputMixin(unittest.TestCase):
    def setUp(self):
        self.input_list = [12, 65, 23, 67, 45, 78, 90, 34, 23, 67, 45]


class InsertionSortTestSuite(SortingInputMixin):
    """
        Insertion Sort Test Case
    """

    def test_insertion_sort(self):
        instance = InsertionSort(self.input_list)
        output_list = instance.sort()
        self.assertEqual(sorted(self.input_list), output_list)

        output_list = instance.sort(reverse=True)
        self.assertEqual(sorted(self.input_list, reverse=True), output_list)


class SelectionSortTestSuite(SortingInputMixin):
    """
        Selection Sort Test Case
    """

    def test_selection_sort(self):
        instance = SelectionSort(self.input_list)
        output_list = instance.sort()
        self.assertEqual(sorted(self.input_list), output_list)

        output_list = instance.sort(reverse=True)
        self.assertEqual(sorted(self.input_list, reverse=True), output_list)



if __name__ == '__main__':
    unittest.main()


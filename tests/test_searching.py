from .context import *
import unittest


class SearchInputMixin(unittest.TestCase):
    def setUp(self):
        self.input_list = [12,34,23,56,45,67]


class LinearSearchTestSuite(SearchInputMixin):
    """
        Linear Search Test Case
    """

    def test_linear_search(self):
        instance = LinearSearch(self.input_list)
        index = instance.search_item(23)
        self.assertEqual(self.input_list.index(23), index)


if __name__ == '__main__':
    unittest.main()

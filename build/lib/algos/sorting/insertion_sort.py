"""
    This is the sorting module that has all the basic operations specified that will be used frquently in programming
"""

class InsertionSort(object):
    """
	Takes two values and swaps them
        Basic Usage:

        Simply Sorting

	    >>> instance = InsertionSort([12, 65, 23, 67, 45, 78, 90, 34, 23, 67, 45])
        >>> sorted_list = instance.sort()

        Sorting in the Reverse Order

        >>> instance = InsertionSort([12, 65, 23, 67, 45, 78, 90, 34, 23, 67, 45])
        >>> sorted_list = instance.sort(reverse=True)
    """
    def __init__(self, *args):
        self.input_list = args

    def sort(self, reverse=False):
        for i in range(1, len(self.input_list)):
            key = self.input_list[i]
            j = i - 1
            while j>=0 and self.input_list[j]>key:
                self.input_list[j+1] = self.input_list[j]
                j -= 1
            self.input_list[j+1] = key

        return self.input_list

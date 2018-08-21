'''
Module demonstrates quick sort
'''

import unittest
import random

def quicksort(data):
    'Function implements quicksort algorithm'
    if len(data) <= 1:
        return data
    pivot = data[random.randint(0, len(data)-1)]
    less = quicksort([element for element in data if element < pivot])
    greater = quicksort([element for element in data if element > pivot])
    return less + [element for element in data if element == pivot] + greater

class QuickSortTest(unittest.TestCase):
    'Class implements quick sort test'

    def test_empty_list_sort(self):
        'Function tests sorting empty list'
        self.assertEqual([], quicksort([])) 

    def test_one_element_sort(self):
        'Function tests one-element list sort'
        self.assertEqual(['A'], quicksort(['A']))

    def test_data_not_mutated(self):
        'Function tests that quicksort doesnt mutates data'
        data = [3, 5, 7, 0, 1]
        sorted_data = quicksort(data)
        self.assertEqual([0, 1, 3, 5, 7], sorted_data)
        self.assertNotEqual(id(data), id(sorted_data))

    def test_sort_not_sorted(self):
        'Test sorting of a not-sorted array'
        data = [-40, 5, 7, 0, 1, -50]
        self.assertEqual([-50, -40, 0, 1, 5, 7], quicksort(data))

if __name__ == '__main__':
    unittest.main()

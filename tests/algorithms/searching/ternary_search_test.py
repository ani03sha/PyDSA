import unittest

from algorithms.searching.ternary_search import ternary_search


class TestTernarySearch(unittest.TestCase):
    def test_ternary_search(self):
        # Test case 1: Search for an element present in the list
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(ternary_search(nums, 5), 4)

        # Test case 2: Search for an element not present in the list
        nums = [10, 20, 30, 40, 50]
        self.assertEqual(ternary_search(nums, 60), None)

        # Test case 3: Search in an empty list
        nums = []
        with self.assertRaises(Exception):
            ternary_search(nums, 0)

        # Test case 4: Search in a list with a single element
        nums = [42]
        self.assertEqual(ternary_search(nums, 42), 0)


if __name__ == '__main__':
    unittest.main()

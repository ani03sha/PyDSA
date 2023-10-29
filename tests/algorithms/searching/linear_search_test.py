import unittest
from algorithms.searching.linear_search import linear_search


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        nums = [4, 2, 7, 1, 9, 5]
        self.assertEqual(linear_search(nums, 7), 2)

        nums = None
        with self.assertRaises(Exception):
            linear_search(nums, 3)

        with self.assertRaises(Exception):
            linear_search([], 5)

        nums = [9]
        self.assertEqual(linear_search(nums, 9), 0)

        nums = [6]
        self.assertEqual(linear_search(nums, 9), None)

        nums = [3, 7, 2, 7, 9]
        self.assertEqual(linear_search(nums, 7), 1)

        nums = list(range(1000000))
        self.assertEqual(linear_search(nums, 999999), 999999)

        nums = [-1, -5, -3, -8, -10]
        self.assertEqual(linear_search(nums, -8), 3)

        nums = ['apple', 3, 'banana', True]
        self.assertEqual(linear_search(nums, 'banana'), 2)

        nums = [1.5, 3.7, 2.8, 5.2]
        self.assertEqual(linear_search(nums, 2.8), 2)


if __name__ == '__main__':
    unittest.main()

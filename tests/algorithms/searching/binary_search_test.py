import unittest
from algorithms.searching.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 1), 0)

        nums = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 5), 4)

        nums = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 3), 2)

        nums = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 0), None)

        nums = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 6), None)

        with self.assertRaises(Exception):
            binary_search([], 42)

        nums = [42]
        self.assertEqual(binary_search(nums, 42), 0)

        nums = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(binary_search(nums, 2), 1)

        nums = list(range(1, 1001))
        self.assertEqual(binary_search(nums, 750), 749)

        nums = [1.1, 2.2, 3.3, 4.4, 5.5]
        self.assertEqual(binary_search(nums, 3.3), 2)


if __name__ == '__main__':
    unittest.main()

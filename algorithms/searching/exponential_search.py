"""
nums - source array
target - value to be searched

Time complexity - O(log[2] N)
Space complexity - O(1)
"""


def exponential_search(nums, target):
    # Check if the list is null or empty
    if nums is None or len(nums) == 0:
        raise Exception("List cannot be null or empty")
    # Check if the element is found at the first position
    if nums[0] == target:
        return 0
    # Length of the list
    n = len(nums)
    # Find the range for binary search
    index = 1
    while index < n and nums[index] <= target:
        index *= 2
    # Perform binary search on the above range
    return binary_search(nums, index, n, target)


def binary_search(nums, index, n, target):
    # Left and right pointers
    left = index // 2
    right = min(index, n - 1)
    # Traverse through the array until the two
    # pointers meet
    while left <= right:
        # Middle pointer
        middle = left + (right - left) // 2
        # Check if the element at the middle index is
        # equal to the target value
        if nums[middle] == target:
            return middle
        # If the target value is less than the middle element,
        # then we are too far right, and we need to search in
        # left half of the list
        elif nums[middle] > target:
            right = middle - 1
        # If the target value is more than the middle element,
        # then we are too far left, and we need to search in
        # right half of the list
        else:
            left = middle + 1
    # If we reach here, it means the target is not found in
    # the list, we will return None
    return None

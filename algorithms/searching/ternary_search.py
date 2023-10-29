"""
nums - source array
target - value to be searched

Time complexity - O(log[3] N)
Space complexity - O(1)
"""


def ternary_search(nums, target):
    # Check if the list is not null or is empty
    if nums is None or len(nums) == 0:
        raise Exception("List cannot be null or empty")
    # Length of the list
    n = len(nums)
    # Left and right pointers
    left = 0
    right = n - 1
    # Traverse the list until the two pointers meet
    while left <= right:
        # Calculate middle_one and middle_two
        middle_one = left + (right - left) // 3
        middle_two = right - (right - left) // 3
        # Check if the target is preset at either of
        # the middle pointers
        if nums[middle_one] == target:
            return middle_one
        if nums[middle_two] == target:
            return middle_two
        # Check if the target is present between left and
        # middle_one pointers
        if target < nums[middle_one]:
            right = middle_one - 1
        # Check if the target is present between middle_two
        # and right pointers
        elif target > nums[middle_two]:
            left = middle_two + 1
        # If the target lies between middle_one and middle_two
        else:
            left = middle_one + 1
            right = middle_two - 1
    # If we reach here, it means target is not found in the list
    return None

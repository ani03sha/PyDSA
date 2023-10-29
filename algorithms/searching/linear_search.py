"""
nums - source array
target - value to be searched

Time complexity - O(N)
Space complexity - O(1)
"""


def linear_search(nums, target):
    # Check if the list is null or empty
    if nums is None or len(nums) == 0:
        raise Exception("List cannot be null or empty")
    # Loop through the list with every element
    for index in range(len(nums)):
        # check if the current element is equal to the target
        if nums[index] == target:
            return index
    # If the element is not found, return None
    return None

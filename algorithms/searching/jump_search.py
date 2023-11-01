import math

"""
nums - source array
target - value to be searched

Time complexity - O(sqrt(N))
Space complexity - O(1)
"""


def jump_search(nums, target):
    # Check if the list is null or empty
    if nums is None or len(nums) == 0:
        raise Exception("List cannot be null or empty")
    # Length of the list
    n = len(nums)
    # Size of the step we need to jump
    step = int(math.sqrt(n))
    previous = 0
    # Loop until we find the appropriate range
    while nums[min(step, n) - 1] < target:
        previous = step
        step += int(math.sqrt(n))
        # Target element is not present in the list
        if previous >= n:
            return None
    # Now, perform linear search on the list in the range
    while nums[previous] < target:
        previous += 1
        if previous == min(step, n):
            return None
    if nums[previous] == target:
        return previous
    return None

def binary_search(nums, target):
    # length of the list
    n = len(nums)
    # Left and right pointers
    left = 0
    right = n - 1
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

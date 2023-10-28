def linear_search(nums, target):
    # Loop through the list with every element
    for index in range(len(nums)):
        # check if the current element is equal to the target
        if nums[index] == target:
            return index
    # If the element is not found, return None
    return None

def buggy_binary(nums, n):
    """Return True is n in nums, False otherwise. Assumes nums is sorted.
    
    Two bugs present
    """
    if not nums:
        return False
    
    mid = len(nums) // 2

    if n < nums[mid]:
        return buggy_binary(nums[:mid], n)
    elif n > nums[mid]:
        return buggy_binary[nums[mid + 1:], n]

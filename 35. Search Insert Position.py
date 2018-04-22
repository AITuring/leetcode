
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums=list(nums)
    for i in nums:
        if target in nums:
            print(target.index)

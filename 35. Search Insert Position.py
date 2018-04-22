
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if target in nums:
        print(nums.index(target))
        return nums.index(target)
    else:
        nums.append(target)
        print(nums)
        nums.sort()
        print(nums)
        return nums.index(target)

nums=[1,2,3,4]
searchInsert(nums,5)

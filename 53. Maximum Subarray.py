def maxSubArray(nums):
    ans=nums[0]
    sum=nums[0]
    for i in range(1,len(nums)):
        sum=max(sum+nums[i],nums[i])
        if sum>ans:
            ans=sum
    return ans



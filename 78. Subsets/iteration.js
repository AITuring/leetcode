var purchasePlans = function(nums, target) {
    nums.sort((a,b)=>a-b)
    let count=0
    let begin=0
    let end=nums.length-1
    while(begin<end){
        let sum=nums[begin]+nums[end]
        if (sum<=target){
            count++
            begin++
        }else{
            end--
        }
    }
    return count

};

nums = [2,2,1,9], target = 10
console.log(purchasePlans(nums,target))
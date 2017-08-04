def twoSum( nums, target):
    dic = {}
    for i in range(0, len(nums)):
        if nums[i] in dic:
            return [dic[nums[i]], i]
        else:
            dic[target - nums[i]] = i

nums=[3,2,4]
target=6
z=twoSum(nums,target)
print z
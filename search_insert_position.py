
def searchInsert(nums,target):
    l=len(nums)
    if target<nums[0]:
        return 0
    elif target in nums:
        for i in range(l):
            if target==nums[i]:
                return i
    elif target>max(nums):
        return l
    else:
        for i in  range(l):
            if target>nums[i] and target<max(nums)and target<nums[i+1]:
                return i+1
print(searchInsert(nums=[1,2,3,4]),target=22)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k=len(nums)
        if k<=1:
            return k
        length=1
        count=1
        nums.sort()
        element=nums[0]
        for i in range(1,k):
            if nums[i-1]==nums[i]:
                continue
            if nums[i]==element+1:
                count+=1
                element=nums[i]
            else:
                element=nums[i]
                length=max(length,count)
                count=1
        return max(length,count)

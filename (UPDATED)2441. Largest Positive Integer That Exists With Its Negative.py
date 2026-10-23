class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums=set(nums)
        ans=-1
        for i in nums:
            if i>0 and -i in nums:
                ans=max(ans,i)
        return ans

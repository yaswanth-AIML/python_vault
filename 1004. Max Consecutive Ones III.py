class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        max1=0
        zero=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            while zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            max1=max(max1,i-l+1)
        return max1

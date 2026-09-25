class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        out=0
        l=0
        product=1
        for i in range(len(nums)):
            product*=nums[i]
            while product>=k:
                product/=nums[l]
                l+=1
            out+=i-l+1
        return out

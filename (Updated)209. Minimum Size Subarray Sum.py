class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        else:
            ans=float('inf')
            slide=0
            k=0
            last=0
            for i in range(len(nums)):
                slide+=nums[i]
                k+=1
                while slide>=target:
                    ans=min(ans,k)
                    slide-=nums[last]
                    last+=1
                    k-=1
        if ans==float('inf'):
            return 0
        else:
            return ans

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        else:
            sum1=0
            last=0
            k=0
            ans = float('inf')
            for i in range(len(nums)):
                sum1+=nums[i]
                k+=1
                while sum1>=target:
                    ans=min(ans,k)
                    k-=1
                    sum1-=nums[last]
                    last+=1
                if sum1==target:
                    return k
        if ans==float('inf'):
            return 0
        else:
            return ans

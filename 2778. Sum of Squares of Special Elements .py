class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum1=0
        k=len(nums)
        for i in range(1,len(nums)+1):
            if k%i==0:
                sum1+=nums[i-1]**2
        return sum1

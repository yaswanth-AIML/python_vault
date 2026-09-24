class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max1=0
        sum1=0
        for i in nums:
            if i==1:
                sum1+=1
            else:
                max1=max(max1,sum1)
                sum1=0
        max1=max(max1,sum1)
        return max1

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums)>1:
            li=[]
            for i in range(len(nums)-1):
                li.append((nums[i]+nums[i+1])%10)
            nums=li
        return nums[0]

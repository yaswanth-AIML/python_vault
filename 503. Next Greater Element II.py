class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=nums+nums
        for i in range(len(nums)):
            k=i+1
            while k<len(n) and n[i]>=n[k]:
                k+=1
            if k<len(n):
                nums[i]=n[k]
            else:
                nums[i]=-1
        return nums

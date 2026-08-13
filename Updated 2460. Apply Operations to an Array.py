class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        while i<n-1: 
            if nums[i]==nums[i+1]:
                nums[i]=nums[i+1]*2
                nums[i+1]=0
                i+=2
            else:
                i+=1
        li=[0]*n
        count=0
        for i in range(n):
            if nums[i]!=0:
                li[count]=nums[i]
                count+=1
        return li

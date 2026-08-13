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
        li=[]
        count=0
        for i in nums:
            if i!=0:
                li.append(i)
            else:
                count+=1
        for i in range(count):
            li.append(0)
        return li

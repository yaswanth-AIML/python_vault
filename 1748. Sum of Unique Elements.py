class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        ans=0
        for k,v in di.items():
            if v==1:
                ans+=k
        return ans

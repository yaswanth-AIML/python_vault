class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        ap={}
        for i in nums:
            if i in ap:
                count+=ap[i]
                ap[i]+=1
            else:
                ap[i]=1
        return count

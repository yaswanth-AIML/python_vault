class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        li={}
        for i in nums:
            li[i]=li.get(i,0)+1
        h={}
        for i in li.values():
            h[i]=h.get(i,0)+1
        for i in nums:
            if h[li[i]]==1:
                return i
        return -1

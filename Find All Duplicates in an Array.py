class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        se=set()
        dup=[]
        for i in nums:
            if i in se:
                dup.append(i)
            else:
                se.add(i)
        return dup

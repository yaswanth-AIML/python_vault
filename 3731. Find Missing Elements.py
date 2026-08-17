class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max1=max(nums)
        min1=min(nums)
        li=[]
        for i in range(min1,max1):
            if i not in nums:
                li.append(i)
        return li

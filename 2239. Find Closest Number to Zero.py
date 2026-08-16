class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        l=nums[0]
        for i in nums:
            if abs(i)<abs(l):
                l=i
            elif abs(i)==abs(l) and i>l:
                l=i
        return l

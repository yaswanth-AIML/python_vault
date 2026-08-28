class Solution:
    def findMin(self, nums: List[int]) -> int:
        min1=nums[0]
        for i in nums:
            if i<min1:
                min1=i
        return min1

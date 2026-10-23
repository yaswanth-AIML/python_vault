class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        while nums:
            k=max(nums)
            if -k in nums:
                return k
            else:
                nums.remove(k)
        return -1

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while True:
            if original in nums:
                original=2*original
            else:
                return original

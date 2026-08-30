class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k=len(nums)
        i=0
        while i<k:
            nums.append(nums[i])
            i+=1
        return nums

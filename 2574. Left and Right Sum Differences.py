class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            li.append(abs(left-right))
        return li

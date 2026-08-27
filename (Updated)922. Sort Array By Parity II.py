class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        le=[0]*len(nums)
        even=0
        odd=1
        for i in nums:
            if i%2==0:
                le[even]=i
                even+=2
            else:
                le[odd]=i
                odd+=2
        return le

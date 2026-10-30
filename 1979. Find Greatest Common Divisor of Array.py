class Solution:
    def findGCD(self, nums: list[int]) -> int:
        great=max(nums)
        small=min(nums)
        maxi=0
        if great==small:
            return great
        for i in range(1,small+1):
            if great%i==0 and small%i==0:
                maxi=max(maxi,i)
        return maxi

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0
        ans=0
        for i in nums:
            if i==0:
                right=total-left
                if left==right:
                    ans+=2
                if abs(left-right)==1:
                    ans+=1
            left+=i
        return ans

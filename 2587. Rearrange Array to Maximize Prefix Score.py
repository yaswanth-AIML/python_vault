class Solution:
    def maxScore(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        sum1=0
        score=0
        for i in nums:
            sum1+=i
            if sum1>0:
                score+=1
            else:
                break
        return score

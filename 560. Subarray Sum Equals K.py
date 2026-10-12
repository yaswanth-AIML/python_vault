class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        di={0:1}
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            minus=sum1-k
            if minus in di:
                count+=di[minus]
            di[sum1]=di.get(sum1,0)+1
        return count

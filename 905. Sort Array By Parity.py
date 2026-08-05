class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        l2=[]
        for i in nums:
            if i%2==0:
                l.append(i)
            else:
                l2.append(i)
        return list(l+l2)

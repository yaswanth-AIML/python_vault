class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        li=[0]*len(nums)
        pos=0
        neg=1
        for i in nums:
            if i>0:
                li[pos]=i
                pos+=2
            else:
                li[neg]=i
                neg+=2
        return li

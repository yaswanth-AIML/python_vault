class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        li=[[]]
        for i in nums:
            for j in list(li):
                li.append(j+[i])
        return li

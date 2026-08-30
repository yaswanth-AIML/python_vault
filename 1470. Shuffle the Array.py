class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        li=[]
        slow=0
        fast=n
        while slow<n:
            li.append(nums[slow])
            li.append(nums[fast])
            slow+=1
            fast+=1
        return li

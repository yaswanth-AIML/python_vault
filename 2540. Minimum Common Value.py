class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums2=set(nums2)
        ans=float('inf')
        for i in nums1:
            if i in nums2:
                ans=min(i,ans)
        if ans!=float('inf'):
            return ans
        else:
            return -1

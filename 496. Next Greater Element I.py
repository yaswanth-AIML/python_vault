class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1=len(nums1)
        len2=len(nums2)
        li=[]
        for i in range(len1):
            j=0
            while nums1[i]!=nums2[j]:
                j+=1
            j+=1
            for k in range(j,len2):
                if nums1[i]<nums2[k]:
                    li.append(nums2[k])
                    break
            else:
                li.append(-1)
        return li

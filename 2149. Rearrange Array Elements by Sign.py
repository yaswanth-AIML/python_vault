class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi=[]
        nega=[]
        for i in nums:
            if i>0:
                posi.append(i)
            else:
                nega.append(i)
        main=[0]*len(nums)
        j=0
        for i in posi:
            main[j]=i
            j+=2
        k=1
        for i in nega:
            main[k]=i
            k+=2
        return main

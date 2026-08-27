class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=[]
        l2=[]
        l3=[0]*len(nums)
        for i in nums:
            if i%2==0:
                l.append(i)
            else:
                l2.append(i)
        i=0
        k=0
        while i<len(l3) and k<len(l):
            l3[i]=l[k]
            k+=1
            i+=2
        i=1
        k=0
        while i<len(l3) and k<len(l2):
            l3[i]=l2[k]
            i+=2
            k+=1
        return l3

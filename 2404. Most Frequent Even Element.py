class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        freq=0
        num=float('inf')
        for k,v in di.items():
            if k%2==0:
                if freq==v:
                    num=min(num,k)
                elif freq>v:
                    pass
                else:
                    freq=v
                    num=k
        if num==float('inf'):
            return -1
        else:
            return num

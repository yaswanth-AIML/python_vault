class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        di={}
        for i in nums:
            h=f"{i}"
            if h in di:
                di[h]+=1
            else:
                di[h]=1
        li=[]
        for y,v in di.items():
            li.append([v,y])
        sorted_di=sorted(li,reverse=True)
        if len(li)<=1:
            return [int(sorted_di[0][1])] 
        else:
            ki=[]
            for i in range(k):
                ki.append(int(sorted_di[i][1]))
            return ki

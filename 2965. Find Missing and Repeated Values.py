class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        li=[]
        for i in grid:
            for j in i:
                li.append(j)
        k=set()
        h=[]
        for i in li:
            if i in k:
                h.append(i)
            k.add(i)
        for i in range(1,len(li)+1):
            if i not in k:
                h.append(i)
        return h

class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        di={}
        for i in range(len(costs)):
            di[i]=costs[i][0]-costs[i][1]
        sorted1=sorted(di,key=di.get)
        n=len(costs)//2
        ans=0
        for i in range(n):
            ans+=costs[sorted1[i]][0]
        for j in range(n,len(costs)):
            ans+=costs[sorted1[j]][1]
        return ans

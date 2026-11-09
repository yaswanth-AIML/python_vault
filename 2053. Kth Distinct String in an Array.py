class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        di={}
        for i in arr:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        h=1
        for ke,v in di.items():
            if v==1 and h==k:
                return ke
            if v==1:
                h+=1
        return ""

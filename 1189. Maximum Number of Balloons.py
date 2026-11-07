class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        di={}
        for i in text:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        li=[]
        ne=set("balloon")
        d={}
        for k,v in di.items():
            if k in ne:
                d[k]=v
        s="balloon"
        if len(d)==len(ne):
            for k,v in d.items():
                if k=='l' or k=='o':
                    if v>=2:
                        li.append(v//2)
                    if v<2:
                        return 0
                else:
                    li.append(v)
        else:
            return 0
        return min(li)

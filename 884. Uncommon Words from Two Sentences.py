class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        di={}
        k=""
        for i in s1:
            if i!=" ":
                k=k+i
            else:
                if k in di:
                    di[k]+=1
                else:
                    di[k]=1
                k=""
        if k in di:
            di[k]+=1
        else:
            di[k]=1
        h=""
        for j in s2:
            if j!=" ":
                h=h+j
            else:
                if h in di:
                    di[h]+=1
                else:
                    di[h]=1
                h=""
        if h in di:
            di[h]+=1
        else:
            di[h]=1
        li=[]
        for k,v in di.items():
            if v==1:
                li.append(k)
        return li

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s)<len(p):
            return []
        k=[]
        d1={}
        for i in p:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        d2={}
        for i in range(len(p)):
            if s[i] in d2:
                d2[s[i]]+=1
            else:
                d2[s[i]]=1
        last=len(p)
        first=0
        while last<len(s):
            if d1==d2:
                k.append(first)
            d2[s[first]]-=1
            if d2[s[first]]==0:
                del d2[s[first]]
            if s[last] in d2:
                d2[s[last]]+=1
            else:
                d2[s[last]]=1
            first+=1
            last+=1
        if d1==d2:
            k.append(first)
        return k

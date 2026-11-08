class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k=[]
        first=0
        last=len(p)-1
        p=sorted(p)
        while last<len(s):
            h=sorted(s[first:last+1])
            if p==h:
                k.append(first)
            first+=1
            last+=1
        return k

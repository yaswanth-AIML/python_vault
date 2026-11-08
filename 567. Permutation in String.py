class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d1={}
        for i in s1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        d2={}
        for i in range(len(s1)):
            if s2[i] in d2:
                d2[s2[i]]+=1
            else:
                d2[s2[i]]=1
        first=0
        last=len(s1)
        while last<len(s2):
            if d1==d2:
                return True
            d2[s2[first]]-=1
            if d2[s2[first]]==0:
                del d2[s2[first]]
            if s2[last] in d2:
                d2[s2[last]]+=1
            else:
                d2[s2[last]]=1
            last+=1
            first+=1
        if d1==d2:
            return True 
        return False 

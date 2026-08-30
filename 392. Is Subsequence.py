class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        h=s[0]
        k=0
        for i in t:
            if i==h:
                k+=1
                if k==len(s):
                    return True
                h=s[k]
        return False     

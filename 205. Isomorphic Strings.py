class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        li={}
        for i in range(len(s)):
            if s[i] in li:
                if li[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in li.values():
                    return False
            li[s[i]]=t[i]
        return True

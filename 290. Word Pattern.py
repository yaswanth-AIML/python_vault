class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li=s.split(" ")
        if len(li)!=len(pattern):
            return False
        di={}
        for i in range(len(pattern)):
            if pattern[i] in di:
                if di[pattern[i]]!=li[i]:
                    return False
            else:
                if li[i] in di.values():
                    return False
            di[pattern[i]]=li[i]
        return True

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        s=list(s)
        right=len(s)-1
        while left<=right:
            if s[left].isalpha() and s[right].isalpha():
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left].isalpha() and not s[right].isalpha():
                right-=1
            elif not s[left].isalpha() and s[right].isalpha():
                left+=1
            else:
                right-=1
                left+=1
        return "".join(s)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vo=set('aeiouAEIOU')
        left=0
        s=list(s)
        right=len(s)-1
        while left<=right:
            if s[left] in vo and s[right] in vo:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left] in vo and s[right] not in vo:
                right-=1
            else:
                left+=1
        return "".join(s)

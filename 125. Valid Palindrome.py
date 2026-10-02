class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=[]
        for c in s:
            if c.isalnum():
                k.append(c.lower())
        s =''.join(k)
        right=len(s)-1
        left=0
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True

class Solution:
    def longestPalindrome(self, s: str) -> int:
        di={}
        for i in s:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        k=0
        ans=0
        for i in di.values():
            if i%2==0:
                ans+=i
            elif k==0:
                ans+=i
                k+=1
            else:
                ans+=i-1
        return ans

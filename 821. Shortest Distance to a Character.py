class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        li=[]
        left=0
        right=0
        while right<len(s):
            if s[right]==c:
                k=left
                for i in range(k,right+1):
                    k=right-left
                    if li:
                        k=min(k,li[-1]+1) 
                    li.append(k)
                    left+=1
            right+=1
        while left<len(s):
            li.append(li[-1]+1)
            left+=1
        return li

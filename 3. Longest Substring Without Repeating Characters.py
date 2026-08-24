class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        li=[]
        for i in s:
            if i in li:
                dup=li.index(i)
                li=li[dup+1:]
            li.append(i)
            max1=max(max1,len(li))
        return max1

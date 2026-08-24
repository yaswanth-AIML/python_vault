class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        length=0
        li=[]
        for i in s:
            if i in li:
                dup=li.index(i)
                new=dup+1
                li=li[new:]
            li.append(i)
            length+=1
            max1=max(max1,len(li))
        return max1

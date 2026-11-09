class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        di={}
        main=words1+words2
        for i in main:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        count=0
        words1=set(words1)
        words2=set(words2)
        for k,v in di.items():
            if v==2 and k in words1 and k in words2:
                count+=1
        return count

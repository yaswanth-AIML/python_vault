class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        di={}
        for i in words[0]:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        for i in range(1,len(words)):
            ki={}
            for j in words[i]:
                if j in ki:
                    ki[j]+=1
                else:
                    ki[j]=1
            for l in di:
                if l in ki:
                    di[l]=min(di[l],ki[l])
                else:
                    di[l]=0
        li=[]
        for i in di:
            if di[i]>=1:
                for k in range(di[i]):
                    li.append(i)
        return li

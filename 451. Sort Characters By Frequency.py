class Solution:
    def frequencySort(self, s: str) -> str:
        di={}
        for i in s:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        ki=""
        sorted_dic =dict(sorted(di.items(),key=lambda x:x[1],reverse=True))
        for key,value in sorted_dic.items():
            for h in range(value):
                ki+=key 
        return ki

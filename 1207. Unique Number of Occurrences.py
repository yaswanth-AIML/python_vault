class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        di={}
        for i in arr:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        li=set()
        for v in di.values():
            li.add(v)
        if len(li)==len(di):
            return True
        else:
            return False

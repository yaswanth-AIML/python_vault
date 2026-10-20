class Solution:
    def digitCount(self, num: str) -> bool:
        k={}
        for i in num:
            h=int(i)
            k[h]=k.get(h,0)+1
        for i in range(len(num)):
            if int(num[i])!=k.get(i,0):
                return False
        return True 

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum1=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                k=[]
                for h in range(i,j+1):
                    k.append(arr[h])
                if len(k)%2==1:
                    for h in k:
                        sum1+=h
        return sum1

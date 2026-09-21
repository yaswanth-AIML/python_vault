class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum1=[]
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                k=[]
                for h in range(i,j+1):
                    k.append(arr[h])
                sum1.append(k)
        act_sum=0
        for i in sum1:
            if len(i)%2==1:
                for k in i:
                    act_sum+=k
        return act_sum

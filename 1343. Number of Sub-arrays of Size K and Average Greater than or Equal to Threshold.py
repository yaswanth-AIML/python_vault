class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        average=0
        sum1=0
        for i in range(k):
            sum1+=arr[i]
        if sum1/k>=threshold:
            average+=1
        h=k
        l=0
        while h<len(arr):
            sum1-=arr[l]
            sum1+=arr[h]
            if sum1/k>=threshold:
                average+=1
            h+=1
            l+=1
        return average

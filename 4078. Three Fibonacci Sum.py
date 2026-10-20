class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        i,j,k=0,1,1
        while k<=n:
            if i+j+k==n:
                return True
            i=j
            temp=j
            j=k
            k=temp+k
        return False
            

class Solution:
    def isThree(self, n: int) -> bool:
        if n<=2:
            return False
        x=int(n**0.5)
        if x*x!=n:
            return False
        for i in range(2,x):
            if x%i==0:
                return False
        return True

class Solution:
    def isHappy(self, n: int) -> bool:
        k1=set()
        while n!=1:
            if n in k1:
                return False
            k=[]
            k1.add(n)
            while n>0:
                k.append(n%10)
                n=n//10
            sum1=0
            for i in k:
                sum1+=i*i
            n=sum1
        return True

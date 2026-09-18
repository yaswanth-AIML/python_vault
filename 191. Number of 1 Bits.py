class Solution:
    def hammingWeight(self, n: int) -> int:
        bina=format(n,"b")
        sum=0
        for i in bina:
            if i=="1":
                sum+=1
        return sum

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(c**0.5)
        while left<=right:
            k=left*left+right*right
            if k==c:
                return True
            elif k<c:
                left+=1
            else:
                right-=1 
        return False

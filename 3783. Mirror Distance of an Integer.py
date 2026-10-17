class Solution:
    def mirrorDistance(self, n: int) -> int:
        nre=str(n)
        new=int(nre[::-1])
        return abs(n-new)

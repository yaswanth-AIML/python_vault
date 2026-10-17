class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones)>1:
            stones.sort()
            k=stones.pop()
            h=stones.pop()
            if h==k:
                pass
            else:
                stones.append(k-h)
        if len(stones)==1:
            return stones[0]
        else:
            return 0

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        li=prices
        ki=[]
        for i in range(len(prices)):
            while len(ki)>0:
                if prices[i]<=prices[ki[-1]]:
                    h=ki.pop()
                    li[h]=li[h]-prices[i]
                else:
                    break
            ki.append(i)
        return li

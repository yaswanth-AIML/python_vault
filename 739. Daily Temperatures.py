class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        li=[0]*len(temperatures)
        ki=[]
        for i in range(len(temperatures)):
            while len(ki)>0:
                if temperatures[ki[-1]]<temperatures[i]:
                    h=ki.pop()
                    li[h]=i-h
                else:
                    break           
            ki.append(i)
        return li

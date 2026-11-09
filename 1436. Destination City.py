class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        li=set()
        for i in paths:
            li.add(i[0])
        for j in paths:
            if j[1] not in li:
                return j[1]

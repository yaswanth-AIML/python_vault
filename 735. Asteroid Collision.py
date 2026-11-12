class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        li=[]
        ki=[]
        for i in asteroids:
            if i<0:
                if len(ki)==0:
                    li.append(i)
                while len(ki)>0:
                    l=ki.pop()
                    if abs(i)>l:
                        if len(ki)==0:
                            li.append(i)
                            break
                    elif abs(i)==l:
                        break
                    else:
                        ki.append(l)
                        break
            else:
                ki.append(i)
        if len(ki)>0:
            li+=ki
        return li

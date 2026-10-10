class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        numRows=rowIndex+1
        li=[]
        if numRows==1:
            li.append([1])
        elif numRows==2:
            li.append([1])
            li.append([1,1])
        else:
            li.append([1])
            li.append([1,1])
            k=2
            while numRows>k:
                ki=[]
                ki.append(1)
                h=li[k-1]
                i=0
                while i<len(h)-1:
                    ki.append(h[i]+h[i+1])
                    i+=1
                ki.append(1)
                li.append(ki)
                k+=1
        return li[rowIndex]

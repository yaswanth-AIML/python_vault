def recursion(l,r):
    if l>=r:
        return 
    li[l],li[r]=li[r],li[l]
    recursion(l+1,r-1)
li=[1,2,3,4,4,3,1,35,24,67,43,67,6]
recursion(0,len(li)-1)
print(li)

def findUnion(a, b):
    arr=list(set(a+b))
    arr.sort()
    return arr
a=[1,1,33,45,7653,22,1,6,7,9]
b=[1,1,22,33,44,45,667,76,5]
print(findUnion(a,b))

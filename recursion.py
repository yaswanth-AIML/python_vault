def recursion(num,sum):
    if num<1:
        print(sum)
        return
    recursion(num-1,sum+num)
def recursion1(num):
    if num==0:
        return 0
    return num+recursion1(num-1)
def recursion_factorial(num):
    if num==1:
        return 1
    return num*recursion_factorial(num-1)
def recursion_factorial1(num,sum):
    if num==1:
        print(sum)
        return
    recursion_factorial1(num-1,sum*num)
num=int(input("ENTER NUMBER:"))
recursion(num,0)
print(recursion1(num))
recursion_factorial1(num,1)
print("FACTORIAL IS:",recursion_factorial(num))

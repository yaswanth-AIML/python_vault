import random as rd
value=int(input("enter how many multiplications do you want to do"))
k=0
for i in range(value):
    num=rd.randint(1,12)
    num1=rd.randint(1,12)
    print(f"enter {num}*{num1}")
    sum=int(input(""))
    actsum=num*num1
    if actsum==sum:
        k=k+1
print(f"you tell {k} correct answers from {value}")
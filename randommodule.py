import random as r
num=r.randint(1,50)
k=0
print("let me guess the number first")
try:
    level=input("which level do you choose hard or easy:")
except:
    print("invalid input")
else:
    if level.lower()=="hard":
        i=5
    else:
        i=10
    value=int(input("enter the value"))
    while k<=i and value!=num:
        if num>value:
            print("higher than you choose")
            value=int(input())
        elif num<value:
            for i in (1,6):
                if num<value-i:
                    print("lower than your value very close  ")
                value=int(input())
            print("lower than your choose")
            value=int(input())
        elif num==value:
            break
        else:
            print("you are out of choices")
        k=k+1
    if num==value:
        print(f"your value is {value} and computer choice is {num} you win")
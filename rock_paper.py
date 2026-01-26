print("Hi hello")
try:
    user=int(input("enter  1 for rock \n2 for papper \n3 for siccors :"))
except:
    print("enter the correct number")
else:
    import random as rd
    com=rd.randint(1,3)
    print("computer choice ",com)
    if user==com:
        print("draw ",com,'=',user)
    elif user==1 and com==2 :
        print("you loose",com,user)
    elif user==2 and com==3:
        print("you loose",com,user)
    elif user==1 and com==3:
        print('you win')
    elif user==2 and com==1:
        print("you win")
    elif user==3 and com==1:
        print('you loose')
    elif user==3 and com==2:
        print('you win')
    else :
        print("enter the correct one try again")

print("hi hello welcome to \n Pizza Hut")
bill=0
size=input("which pizza do you want S OR M OR L \n S=100,M=100,L=300 :")
if size=='s' or size=='S':
    bill+=100
elif size=='m' or size=='M':
    bill+=200
elif size=='L' or size=='l':
    bill+=300
else:
    print("take the oppropriate size:")
    quit()

pep=input("did you pepparani yes or no :")

if pep=='yes'or pep=='YES'or pep=='Yes':
    if size=='s'or size=='S':
        want=input("the cost of pepproni for small pizza is :30\n if you want say yes or no :")
        if want=='yes':
            bill+=30
    elif size=='m' or size=='M' or size=='l' or size=='L':
        want=input("the cost for pepproni is 50 if you want yes or no :")
        if want=='yes':
            bill+=50
elif pep=='no'or pep=='NO'or pep=='No' :
    print("OK")
else :
    print("enter the appropriate one")
    quit()

che=input("if you want extra cheese then cost is 20 :")
if che=='yes'or che=='YES':
    bill+=20
elif che=='no':
    print('ok')
else :
    print("enter the appropriate one ")
    quit()

print("the total bill is ",bill)

    

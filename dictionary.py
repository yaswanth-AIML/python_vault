def insert(book,op="yes"):
    while op=="yes"or op=="Yes"or op=="YES":
        key=input("enter the key or book name")
        value=int(input("enter the number of book"))
        book=dict({key:value})
        op=input("do you wanna insert another key and value")
    prin2=input("do you wanna print the dictnory yes or no")
    if prin2=="yes"or prin2=="Yes"or prin2=="YES":
        prin(book)
    else:
        quit
def prin(book,prin="yes"):
    if prin=="yes"or prin=="Yes"or prin=="YES":
        print(book)
    else:
        quit 
def delete(book):
    wh="yes"
    while wh=="yes"or wh=="Yes"or wh=="YES":
        dele=input("enter the key to delete")
        print(book.pop(dele))
        wh=input("do you wanna delete another value yes or no") 
book={}
Key=None
value=0
opp=int(input("enter an operation 1)for inserting 2)for printing 3)for deleting"))
if opp==1:
    insert(book)
elif opp==2:
    prin(book)
elif opp==3:
    delete(book)
else:
    print("enter the appropriate choice")
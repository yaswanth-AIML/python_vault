input1=input("enter a string")
string=input1.lower()
dict={}
for strings in string:
    if strings.isalpha():
        if strings in dict:
            dict[strings]+=1
        else :
            dict[strings]=1
def sort_key(item):
    char, count = item
    return (-count, char)
dict1 = sorted(dict.items(), key=sort_key)
print(dict1)
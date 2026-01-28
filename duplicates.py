def duplicates(arr):
        arr1=set()
        arr2=set()
        for i in arr:
            if i not in arr1:
                arr1.add(i)
            else:
                arr2.add(i)
        return list(arr2)
arr=[]
num=int(input("enter the how many elements you wanna enter:"))
for i in range(num):
    num1=(int(input("enter numbers"))) 
    arr.append(num1)
print(duplicates(arr))
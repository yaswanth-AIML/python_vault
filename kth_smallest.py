def kthSmallest(arr, k):
    arr.sort()
    return arr[k-1]
arr=[99,777,888,444,8,9,2,5,6,9,1,4,7,33,88,99,66]
k=int(input("enter the which smallest element you wanna find :"))
print(kthSmallest(arr,k))
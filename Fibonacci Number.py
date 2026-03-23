count=0
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    global count
    count+=1
    sum=fib(n-1)+fib(n-2)
    return sum
n=int(input("Which Value you wanna know the fibbinoci:"))
print(fib(n))
print(f"Total Number of Times Function Called:{count}")

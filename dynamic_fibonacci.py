count=0
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    global count
    count+=1
    if n==0:
        return 0
    if n==1:
        return 1
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
n=int(input("Which Value you wanna know the fibbinoci:"))
print(fib(n))
print(f"Total Number of Times Function Called:{count}")

n=int(input("Enter input"))

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(n):
    print(fib(i))   



def fact(n):
    if n==0 or n==1:
        return 1    
    else:
        return fact(n-1)*n

print(fact(n))
    
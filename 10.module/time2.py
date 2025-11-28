import time
def fib(n):
    a,b,=0,1
    while b<n:
        print(b,end=",")
        a,b=b,a+b
    print()

start=time.time()
fib(1000)
end=time.time()
print(end-start)

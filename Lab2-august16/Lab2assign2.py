# Fibonacci series
def fib(x):
    if x is 0 or x is 1:
        return x
    return fib(x-1) + fib(x-2)


n = int(input("Enter the number of total numbers to be present in Fibonacci series(minimum 1): "))
print("Fibonacci series is: ")
for i in range(n):
    print(fib(i), end=' ')


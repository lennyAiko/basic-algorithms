### FIBONACCI SERIES

def fibonacci(num):
    x = 0
    y = 1
    count = 0
    while count <= num:
        print(x, end=" ")
        fib = x + y
        x = y
        y = fib
        count += 1

fibonacci(12)
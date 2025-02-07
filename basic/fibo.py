def fib(n):
    a, b = 0, 1
    while b < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(a)
        a, b = b, a+b
    return result

def add(a, b):
    return a + b
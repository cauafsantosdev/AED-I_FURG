def fib(n: int):
    if n <= 1:
        return n
    
    return fib(n - 1) + fib(n - 2)


def fib_sequence(n: int):
    for i in range(n+1):
        yield fib(i)


for term in fib_sequence(10):
    print(term)
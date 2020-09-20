def fib(n):

    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    return result

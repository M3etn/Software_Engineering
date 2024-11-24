def fib(n):
    a, b = 1, 1
    for num in range(n):
        yield a
        a, b = b, a + b
n = 256
fibonacci_numbers = list(fib(n))
print(f"{n}-е число Фибоначчи: {fibonacci_numbers[-1]}")
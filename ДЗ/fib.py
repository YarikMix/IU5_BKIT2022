def fibonacci(n):
    if type(n) not in [int]:
        raise TypeError(f"Коэффициент n должен быть натуральным числом!")

    if n <= 0:
        raise ValueError("Коэффициент n должен быть натуральным числом!")

    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

if __name__ == '__main__':
    print(*fibonacci(10))

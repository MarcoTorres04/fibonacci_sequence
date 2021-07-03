from datetime import datetime


def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_d(n, cache: dict = {0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_d(n - 1, cache) + fibonacci_d(n - 2, cache)
    return cache[n]


def fibonacci_l(n, cache: list = [0, 1]):
    if n <= 0:
        return 0
    for num in range(2, n + 1):
        cache.append(cache[num - 1] + cache[num - 2])
    return cache[-1]


if __name__ == '__main__':
    time = datetime.now()
    print(fibonacci(20))
    print(datetime.now() - time)

    time = datetime.now()
    print(fibonacci_d(900))
    print(datetime.now() - time)

    time = datetime.now()
    print(fibonacci_l(900))
    print(datetime.now() - time)

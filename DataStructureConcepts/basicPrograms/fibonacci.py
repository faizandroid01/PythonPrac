def fibonacci(n):
    a, b = 0, 1
    d = [a, b]
    for i in range(n - 2):
        c = a + b
        a, b = b, c
        d.append(c)
    return d


class Sample:
    print(fibonacci(10))

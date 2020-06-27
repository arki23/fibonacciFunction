def Fib(x):
    a = 0
    b = 1

    for k in range(abs(int(x))):
        a, b = b + a, a

    return a

def Fib(a):
    if a == 0:
        return 0
    if a == 1 or a == 2:
        return 1
    else:
        return Fib(a-2) + Fib(a-1)

print(Fib(6))
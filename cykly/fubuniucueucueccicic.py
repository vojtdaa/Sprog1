
co = int(input("Zadej: "))

def Fib(n):
    vysledek = 1
    c1 = 1
    c2 = 1

    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1

    while n-2 > 0:
        
        vysledek += c1
        c1 = c2
        c2 = vysledek
        n -= 1
    return vysledek


print(Fib(co))


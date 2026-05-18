def faktorial(n):
    vysledek = 1
    if n == 0:
        return 1
    
    while n > 1:
        vysledek *= n
        n -= 1
    return vysledek

print(faktorial(0))   # → 1
print(faktorial(3))   # → 6
print(faktorial(5))   # → 120
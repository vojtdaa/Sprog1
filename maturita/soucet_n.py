def secti_do_n(n):
    vysledek = 0

    for i in range(1, n+1):
        vysledek += i

    return vysledek

print(secti_do_n(5))     # → 15
print(secti_do_n(10))    # → 55
print(secti_do_n(100))   # → 5050
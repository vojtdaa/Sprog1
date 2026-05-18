def aritm_posloupnost(a1, d, n):
    vysledek = ""
    for i in range(n):
        vysledek += str(a1+d*i)
        if i != n-1:
            vysledek += " "
    return vysledek

print(aritm_posloupnost(1, 2, 5))     # → '1 3 5 7 9'
print(aritm_posloupnost(10, -3, 4))   # → '10 7 4 1'
print(aritm_posloupnost(0, 5, 3))     # → '0 5 10'
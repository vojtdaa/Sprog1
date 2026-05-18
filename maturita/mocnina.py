def mocnina(z, e):
    vysledek = 1
    for _ in range(e):
        vysledek *= z

    return vysledek

print(mocnina(2, 10))   # → 1024
print(mocnina(3, 4))    # → 81
print(mocnina(5, 0))    # → 1
print(mocnina(7, 3))    # → 343
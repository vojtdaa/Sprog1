def rozdil_mocnin(n):
    soucet = 0
    soucet_mocnin = 0
    for i in range(1, n+1):
        soucet += i
        soucet_mocnin += i**2

    return abs(soucet**2-soucet_mocnin)

print(rozdil_mocnin(10))    # → 2640
print(rozdil_mocnin(100))   # → 25164150
print(rozdil_mocnin(1))     # → 0
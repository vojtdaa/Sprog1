def soucet_seznamu(lst):
    soucet = 0
    for i in lst:
        soucet += i

    return soucet

print(soucet_seznamu([1, 2, 3, 4, 5]))   # → 15
print(soucet_seznamu([-1, -2, -3]))       # → -6
print(soucet_seznamu([]))                 # → 0
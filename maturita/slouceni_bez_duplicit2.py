def slouceni_bez_duplicit(a, b):
    novy = []

    for i in a:
        if i not in novy:
            novy.append(i)
    for i in b:
        if i not in novy:
            novy.append(i)

    return novy


print(slouceni_bez_duplicit([1, 2, 3], [2, 3, 4, 5]))   # → [1, 2, 3, 4, 5]
print(slouceni_bez_duplicit([1, 1, 2, 3], [4, 5]))       # → [1, 2, 3, 4, 5]
print(slouceni_bez_duplicit([1, 2, 3], [1, 2, 3]))        # → [1, 2, 3]
def eratosthenovo_sito(n):
    seznam = [a+2 for a in range(n-1)]
    vysledek = []

    for i in range(len(seznam)):
        if seznam[i] != 0:
            vysledek.append(seznam[i])
            for x in range(i, len(seznam), seznam[i]):
                seznam[x] = 0
        
    return vysledek

print(eratosthenovo_sito(10))   # → [2, 3, 5, 7]
print(eratosthenovo_sito(20))   # → [2, 3, 5, 7, 11, 13, 17, 19]
print(eratosthenovo_sito(1))    # → []
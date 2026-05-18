seznam = [7, 7, 7, 7, 7, 7, 1, 1, 5, 5, 5, 5, 5, 5, 7, 7, 7]

def rle(n):
    if not n:
        return []
    prew = n[0]
    pocet = 1
    vysledek = []

    for i in range(1, len(n)):

        if n[i] == prew:
            pocet += 1
        else:
            vysledek.append([prew, pocet])
            prew = n[i]
            pocet = 1

        if i == len(n)-1:
            vysledek.append([prew, pocet])

    return vysledek

        

print(rle([1, 1, 1, 2, 2, 3]))   # → [[1, 3], [2, 2], [3, 1]]
print(rle([1, 1, 2, 1, 1]))       # → [[1, 2], [2, 1], [1, 2]]
print(rle([]))                    # → []
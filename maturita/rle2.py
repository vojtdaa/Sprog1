def rle(lst):
    vysledek = []
    if not lst:
        return []
    temp = lst[0]
    pocet = 1

    for i in range(1, len(lst)):
        if lst[i] == temp:
            pocet += 1
        else:
            vysledek.append([temp, pocet])
            pocet = 1
            temp = lst[i]

        if i == len(lst)-1:
            vysledek.append([temp, pocet])


    return vysledek

print(rle([1, 1, 1, 2, 2, 3]))   # → [[1, 3], [2, 2], [3, 1]]
print(rle([1, 1, 2, 1, 1]))       # → [[1, 2], [2, 1], [1, 2]]
print(rle([]))                    # → []


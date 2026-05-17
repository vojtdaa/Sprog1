seznam = [1, 2, 3, 4, 5, 4, 5, 7, 8, 5, 6, 9, 8, 7, 5]

def najdi_vsechny(lst, hodnota):
    vyskyt = []

    for i in range(len(lst)):
        if lst[i] == hodnota:
            vyskyt.append(i)

    return vyskyt

print(najdi_vsechny(seznam, 5))
        
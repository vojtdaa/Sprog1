def najdi_vsechny(lst, val):
    vyskyt = []

    for i in range(len(lst)):
        if lst[i] == val:
            vyskyt.append(i)

    return vyskyt

print(najdi_vsechny([1, 3, 2, 3, 4, 3], 3))   # → [1, 3, 5]
print(najdi_vsechny([1, 2, 3], 5))             # → []
print(najdi_vsechny([7, 7, 7], 7))             # → [0, 1, 2]
def slouceni_setrizenych_seznamu(a, b):
    novy = []
    i = 0
    j = 0
    iterace = 0
    while iterace != len(a) + len(b):
        if i < len(a) and a[i] <= b[j]:
            novy.append(a[i])
            i += 1
        elif j < len(b):
            novy.append(b[j])
            j += 1
        iterace += 1

    return novy

print(slouceni_setrizenych_seznamu([1, 3, 5], [2, 4, 6]))   # → [1, 2, 3, 4, 5, 6]
print(slouceni_setrizenych_seznamu([1, 1, 3], [1, 2, 4]))    # → [1, 1, 1, 2, 3, 4]
print(slouceni_setrizenych_seznamu([], [1, 2, 3]))            # → [1, 2, 3]
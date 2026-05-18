def otoceni_seznamu(lst):
    novy = []

    for i in range(len(lst)-1, -1, -1):
        novy.append(lst[i])
    
    return novy

print(otoceni_seznamu([1, 2, 3, 4, 5]))     # → [5, 4, 3, 2, 1]
print(otoceni_seznamu([-3, -1, -4, -2]))   # → [-2, -4, -1, -3]
print(otoceni_seznamu([42]))               # → [42]
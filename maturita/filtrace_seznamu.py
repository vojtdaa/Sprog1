def filtrace_seznamu(lst, val):
    vysledek = []

    for i in lst:
        if i > val:
            vysledek.append(i)

    return vysledek

print(filtrace_seznamu([1, 5, 2, 8, 3, 7], 3))   # → [5, 8, 7]
print(filtrace_seznamu([-2, 5, -1, 8, 0], 0))     # → [5, 8]
print(filtrace_seznamu([1, 2, 3], 10))             # → []
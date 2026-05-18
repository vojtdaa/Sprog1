def nejdelsi_serie(n):
    max = 0
    pocet = 1
    temp = None
    for i in n:
        if i == temp:
            pocet += 1
        else:
            pocet = 1
        if pocet > max:
            max = pocet
        temp = i

    return max

print(nejdelsi_serie('aaabba'))    # → 3
print(nejdelsi_serie('abcdef'))    # → 1
print(nejdelsi_serie('aabbbbcc'))  # → 4
print(nejdelsi_serie(''))          # → 0

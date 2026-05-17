seznam1 = [1, 1, 2, 3]
seznam2 = [2, 3, 4, 4, 5]

def slouceni_bez_duplicit(a, b):
    novy = []
    for i in a:
        if i not in novy:
            novy.append(i)
    for i in b:
        if i not in novy:
            novy.append(i)

    return novy

print(slouceni_bez_duplicit(seznam1, seznam2))
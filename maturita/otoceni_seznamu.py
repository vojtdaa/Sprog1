seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def otoceni_seznamu(lst):
    novy = []
    for i in range(len(lst)-1, -1, -1):
        novy.append(lst[i])

    return novy

print(otoceni_seznamu(seznam))
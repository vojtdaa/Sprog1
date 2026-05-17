seznam1 = [1, 3, 5, 7, 9]
seznam2 = [0, 2, 4, 7, 9, 10, 15]

def slouceni_setrizenych_seznamu(a, b):
    novy = []
    i = 0
    j = 0

    for i in range(len(a)+len(b)):

        if i < len(a) and a[i] <= b[j]:
            novy.append(a[i])
            i +=1
            
        elif j < len(b):
            novy.append(b[j])
            j += 1

    return novy

print(slouceni_setrizenych_seznamu(seznam1,seznam2))


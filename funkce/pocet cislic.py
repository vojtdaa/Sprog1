def pocet_cislic(cislo):
    cislo = abs(cislo)

    if cislo == 0:
        return 1
    
    pocet = 0

    while cislo > 0:
        cislo = cislo // 10
        pocet += 1
    
    return pocet

def pocet_cislic_2(cislo):
    return len(str(abs(cislo)))



print(pocet_cislic(2123))
print(pocet_cislic_2(1645))
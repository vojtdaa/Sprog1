def Delitelnost(cislo, pocet):
    if cislo == 0:
        return "Nelze delit nulou"
    delitelna_cisla = []
    for i in range(1, pocet +1):
        if i % cislo == 0:
            delitelna_cisla.append(i)
    return delitelna_cisla


print(Delitelnost(0, 15))

def DoBinarni(a):
    vysledek = ""
    mezicislo = a
    if a == 0:
        return 0
    while mezicislo > 0:
        vysledek = str(mezicislo % 2) + vysledek
        mezicislo //= 2

    return vysledek

print(DoBinarni(10))
print(DoBinarni(2))
print(DoBinarni(1))
print(DoBinarni(0))
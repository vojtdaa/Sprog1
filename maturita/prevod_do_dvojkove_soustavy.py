def DoBinarni(a, b):
    vysledek = ""
    mezicislo = a
    if a == 0:
        return 0
    while mezicislo > 0:
        vysledek = str(mezicislo % b) + vysledek
        mezicislo //= b

    return vysledek

print(DoBinarni(1166, 6)) #nyni kod prevadi z 10-soustavy do b-soustavy
'''print(DoBinarni(2))
print(DoBinarni(1))
print(DoBinarni(0))'''
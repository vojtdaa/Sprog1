def Secti(a):
    vysledek = 0
    while a != 0:
        vysledek += a % 10
        a //= 10

    return vysledek



print(Secti(111))
print(Secti(1212))
print(Secti(999))
def validuj_heslo(heslo):
    velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cisla = "0123456789"

    velke_pismeno = False
    cislice = False

    temp = None

    if len(heslo) <= 8:
        return False

    for i in heslo:
        if not velke_pismeno:
            if i in velka:
                velke_pismeno = True
        if not cislice:
            if i in cisla:
                cislice = True

        if i == temp:
            return False
        
        temp = i
        
        if velke_pismeno and cislice:
            return True
        
    return False

print(validuj_heslo('Heslo1234'))     # → True
print(validuj_heslo('Heslo12'))       # → False  (jen 8 znaků, musí být více)
print(validuj_heslo('heslo1234!'))    # → False  (chybí velké písmeno)
print(validuj_heslo('HHeslo1234'))    # → False  (dvě H za sebou)
def je_silne_heslo(heslo):
    mala_pismena = "abcdefghijklmnopqrstuvwxyz"
    velka_pismena = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cislice_seznam = "0123456789"

    delka = False
    velky_znak = False
    maly_znak = False
    cislice = False


    if len(heslo) >= 8:
        delka = True

    for i in heslo:
        if not velky_znak:
            if i in velka_pismena:
                velky_znak = True

        if not maly_znak:
            if i in mala_pismena:
                maly_znak = True

        if not cislice:
            if i in cislice_seznam:
                cislice = True
        
        if velky_znak and maly_znak and cislice and delka:
            return True
        
    return False

print(je_silne_heslo('Heslo123'))   # → True
print(je_silne_heslo('heslo123'))   # → False  (chybí velké písmeno)
print(je_silne_heslo('HESLO123'))   # → False  (chybí malé písmeno)
print(je_silne_heslo('Abc1'))       # → False  (příliš krátké)
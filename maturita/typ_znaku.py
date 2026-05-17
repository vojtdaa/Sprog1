mala = "abcdefghijklmnopqrstuvwxyz"
velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cisla = "0123456789"

def typ_znaku(znak):
    if znak in mala:
        return "male"
    if znak in velka:
        return "velke"
    if znak in cisla:
        return "cislice"
    
    else:
        return "specialni znak"

print(typ_znaku('a'))   # → 'malé písmeno'
print(typ_znaku('A'))   # → 'velké písmeno'
print(typ_znaku('5'))   # → 'číslice'
print(typ_znaku('!'))   # → 'speciální znak'
print(typ_znaku(' '))   # → 'speciální znak'
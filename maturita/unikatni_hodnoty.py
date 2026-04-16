# Poskytne pristup ke knihovne random pro vyuziti funkce random.randint
import random

# Nacte cele cislo od uzivatele reprezentujici delku seznamu
delka_seznamu = int(input("Zadej delku seznamu: "))

# Tento seznam bude slouzit jako vysledny seznam unikatnich hodnot
unikatni_hodnoty = []

# Vytvori seznam o delce zadane uzivatelem obsahujici nahodna cisla v rozmezi 1 -> delka seznamu
seznam = [random.randint(1, 10) for _ in range(delka_seznamu)]

# Vypise puvodni seznam a pocet jeho hodnot
print(f"Seznam: {seznam} ({len(seznam)})")

# Cyklus projde vsechny hodnoty v puvodnim seznamu a v pripade ze se nenachazi v druhem seznamu, tak je tam prida
for i in seznam:
    if i not in unikatni_hodnoty:
        unikatni_hodnoty.append(i)
        

# Vypise vysledeny seznam unikatnich hodnot a pocet techto hodnot
print(f"Unikatni hodnoty: {unikatni_hodnoty} ({len(unikatni_hodnoty)})")
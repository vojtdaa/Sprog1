delka_seznamu = int(input("Zadej delku seznamu: "))
seznam = []
indexy = []

for x in range(1, delka_seznamu+1):

    cislo = int(input(f"Zadej {x}. cislo: "))
    seznam.append(cislo)

wanted = int(input("HLedat cislo: "))

for i in range(len(seznam)):
    if seznam[i] == wanted:
        indexy.append(x)


print(f"Zde hledam: {seznam}")

if len(indexy) > 0:
    print(indexy)
else:
    print("Hledane se nenachazi v seznamu.")
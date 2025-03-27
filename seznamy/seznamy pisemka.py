seznam1 = []
seznam2 = []
seznam3 = []

prvni_delka = int(input("Zadej delku 1. seznamu: "))

for i in range(prvni_delka):
    seznam1.append(int(input(f"Zadej {i+1}. hodnotu: ")))

druha_delka = int(input("Zadej delku 2. seznamu: "))

for i in range(druha_delka):
    seznam2.append(int(input(f"Zadej {i+1}. hodnotu: ")))

treti_delka = prvni_delka + druha_delka

i = 0
pocet = 0

while pocet < treti_delka:
    if i < prvni_delka:
        hodnota1 = seznam1[i]
        seznam3.append(hodnota1)
        pocet+=1

    if i < druha_delka:
        hodnota2 = seznam2[i]
        seznam3.append(hodnota2)
        pocet+=1
    i+=1

print(seznam3)

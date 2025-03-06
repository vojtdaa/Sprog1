delka = int(input("Zadej horni mez: "))

cisla = [True] * delka

cisla[0] = False
cisla[1] = False

for i in range(2, delka):
    for j in range(i*2, delka, i):
        cisla[j] = False

for i in range(delka):
    if cisla[i]:
        print(i)


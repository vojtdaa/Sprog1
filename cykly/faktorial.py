cislo = int(input("zadej prirozene cislo: "))
nasobitel = cislo -1

for x in range(cislo):
    cislo *= nasobitel
    nasobitel -= 1
    if nasobitel == 1:
        break

print(cislo)
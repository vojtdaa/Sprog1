seznam = [1, 2, 4, 6, 5, 5, -5, -10, 5, 4, 7]

vysledek = 0

for i in seznam:
    vysledek += i

print(vysledek)

nejvetsi = seznam[0]

for i in seznam:
    if i > nejvetsi:
        nejvetsi = i

print(nejvetsi)
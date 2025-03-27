slovnik_polozek = {}

pocet_polozek = int(input("pocet polozek: "))

for klic in range(pocet_polozek):
    klicov = str(input(f"zadej {klic+1}. nazev polozky: "))
    slovnik_polozek[klicov]

print(slovnik_polozek.keys)
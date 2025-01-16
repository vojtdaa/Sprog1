cislo = int(input("zadej cislo: "))
neprvocislo = 0

for x in range(1, 100000):
    if x == 1 or x == cislo:
        continue
    else:
        if cislo % x == 0:
            neprvocislo = 1
            break

if neprvocislo:
    print(f"cislo {cislo} neni prvocislo")
else:
    print(f"cislo {cislo} je prvocislo")


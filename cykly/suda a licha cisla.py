







prepinacka = 0
mez = int(input("napiš MEZ: "))

for x in range(1, mez+1):
    if prepinacka == 0:
        print(f"cislo {x} je liche")
        prepinacka = 1
    else:
        print(f"cislo {x} je sude")
        prepinacka = 0
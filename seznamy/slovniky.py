jmeno = (input("zadej jmeno: "))
pocet_znamek = int(input("pocet znamek: "))

zakovska_knizka = {}
znamky = []

#zakovska_knizka[jmeno]

for i in range(pocet_znamek):
    znamky.append(int(input(f"zadej {i+1}. znamku: ")))

zakovska_knizka[jmeno] = znamky
#print(zakovska_knizka.items())

print(f"prumer znamek zaka {jmeno} je {round(sum(znamky)/pocet_znamek, 2)}")
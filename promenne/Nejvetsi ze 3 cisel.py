import math

prvni_cislo = float(input("zadej prvni cislo: "))
druhe_cislo = float(input("zadej druhe cislo: "))
treti_cislo = float(input("zadej treti cislo: "))

if prvni_cislo > (druhe_cislo and treti_cislo):
    print(f"nejvetsi cislo je: {prvni_cislo}")

elif druhe_cislo > (prvni_cislo and treti_cislo):
    print(f"nejvetsi cislo je: {druhe_cislo}")

elif treti_cislo > (prvni_cislo and druhe_cislo):
    print(f"nejvetsi cislo je: {treti_cislo}")
else:
    print("chyba")
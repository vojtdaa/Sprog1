zaklad = int(input("zadej zaklad: "))
exponent = int(input("zadej exponent: "))
cislo = zaklad

for x in range(exponent-1):
    cislo *= zaklad

print(cislo)
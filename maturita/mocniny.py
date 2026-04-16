zaklad = int(input("Zadej zaklad: "))
exponent = int(input("Zadej exponent: "))
cislo = zaklad


for i in range(exponent-1):
    cislo *= zaklad

if exponent < 0:
    cislo = 1/cislo
    
elif exponent == 0:
    cislo = 1

print(cislo)
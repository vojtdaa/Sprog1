cislo = 1362
cislostring = str(cislo)



prvni_cifra = 9

number = 0


for x in cislostring:
    number = int(x)
    while number != prvni_cifra:
        prvni_cifra -= 1

    


print(prvni_cifra)


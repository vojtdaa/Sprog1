# REKURZE

cislo1 = int(input("Zadej prvni zaklad: "))

def Faktorial(cislo):
    if cislo == 0:
        return 1
    if cislo == 1:
        return 1
    else:
        return cislo * Faktorial(cislo-1)

vysledek1 = Faktorial(cislo1) 
print(vysledek1)

#----------------------------------------------

#CYKLUS

cislo2 = int(input("Zadej druhy zaklad: "))
vysledek2 = 1


for i in range(cislo2-1):
    vysledek2 *= cislo2 - i

print(vysledek2)
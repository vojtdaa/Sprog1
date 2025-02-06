cislo = 0
hodnota = cislo
soucet = 0
fortnite = 0

for cislo in range (1, 10001):
    hodnota = cislo
    while hodnota != 1 and hodnota != 4:

        soucet = 0
        for x in str(hodnota):
            soucet += int(x)**2

        hodnota = soucet
        


    if hodnota == 1:
        print(f"je stastne: {cislo}")
        fortnite += 1

print(fortnite / 10000)
print(f"stastnych cisel je {fortnite / 100}%")


   


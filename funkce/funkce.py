seznam = []

def SudaFunkce(zacatek, konec):
    for i in range(zacatek, konec+1):
        if i%2 == 0:
            seznam.append(i)
    return seznam       
    
            
           

vysledek = SudaFunkce(2, 11)

for x in range(len(seznam)):
    print(vysledek[x])
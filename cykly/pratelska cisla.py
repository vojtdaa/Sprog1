cislo = 0
cislo2 = 0
soucet = 0
soucet2 = 0
last_number = 0

for y in range(2, 10001):
    cislo = y
    soucet = 0
    soucet2 = 0
    for x in range(1,cislo):
        if cislo % x == 0:
          soucet += x
    cislo2 = soucet

    for z in range(1,cislo2): 
        if cislo2 % z == 0:
            soucet2 += z
    if soucet2 == cislo and cislo != cislo2 and cislo > last_number:
        print(f"pratele jsou {cislo, cislo2}")
        last_number = cislo2
    
         
     
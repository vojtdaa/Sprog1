cislo = 0
soucet = 0

for y in range(2, 1001):
  cislo = y
  soucet = 0

  for x in range(1,cislo):
    if cislo % x == 0:
      soucet += x
          
  if soucet == cislo:
    print(cislo)       
     



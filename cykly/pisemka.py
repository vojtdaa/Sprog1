number = 100
count = 0
count2 = 0

for x in range(1, number+1):
    count += x**2

for y in range(1, number+1):
    count2 += y

vysledek = count2**2 - count 
print(vysledek)
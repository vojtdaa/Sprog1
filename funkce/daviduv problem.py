cisla = []
n = 5
k = 3

for i in range(n):
    cisla.append(i+1)

skok = k-1
i = 0
def FindNumber():
    x = 1
    while x > 0:
        if cisla[x] != 0:
            return cisla[x]

    
for i in range(n):
    if cisla[i] == 3:
        cisla[i] = 0
    print(cisla)
    



print(cisla)

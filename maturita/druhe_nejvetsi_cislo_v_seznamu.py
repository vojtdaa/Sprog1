import random

nahodny_seznam = [random.randint(1, 20) for _ in range(10)]

vstupni_seznam = [2,1,1]


def NajdiDruheNejvetsi(seznam):
    max = seznam[0]
    druhy = seznam[0]
    
    for i in range(len(seznam)):
        if seznam[i] > max:
            max = seznam[i]

        if druhy == max:
            if seznam[i] < max:
                druhy = seznam[i]

        if seznam[i] > druhy and seznam[i] < max:
            druhy = seznam[i]

    return druhy

print(nahodny_seznam)
print(NajdiDruheNejvetsi(vstupni_seznam))
            
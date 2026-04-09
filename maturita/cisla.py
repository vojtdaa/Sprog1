seznam = [0, 0, 0, 1, 1, 2, 2, 4, 4, 0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 1]

store = seznam[0]
count = 0
vysledek = []

for i in seznam:
    if i != store:
        vysledek.append(count)
        count = 0

    count += 1
    store = i

print(vysledek)

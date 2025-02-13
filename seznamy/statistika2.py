e = [2, 3, 1, 0, 5, 6, 4, 2, 1, 1, 1]

index = 0
misto = []
wanted_number = int(input("prohledej: "))

for i in e:

    if i == wanted_number:
        misto.append(index)

    if index >= len(e):
        break

    index += 1


print(misto)
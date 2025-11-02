

#plocha 20*5
canvas = ["." for n in range(20)]

for y in range(5):
    for x in range(len(canvas)):
        if y != 2 or x != 10:
            print(canvas[x], end="")
        else:
            print("o", end="")
    print("\n")


def ND(first = 48, second = 18):
    zbytek = first % second
    if zbytek == 0:
        return second
    else:
        return ND(second, zbytek)


print(ND())
print(ND(252, 105))
print(ND(18, 48))
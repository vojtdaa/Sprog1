def Faktorial(a):
    if a < 0:
        return None
    if a == 0:
        return 1
    if a == 1:
        return 1
    return a * Faktorial(a-1)


print(Faktorial(54))
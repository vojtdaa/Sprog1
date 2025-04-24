

def Prevod(hodiny, minuty):
    celkem = 0

    if not isinstance(hodiny, int) or not isinstance(minuty, int):
        return None

    if hodiny >= 0 and minuty >= 0:
        celkem += hodiny *60 + minuty
        return celkem
    
    else:
        return None
    


print(Prevod(10, 2))
print(Prevod(-1, 2))
print(Prevod(1, 2.5))
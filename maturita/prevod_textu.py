mala = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
velka = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

od_uzivatele = str(input("Zadej slovo: "))

def Prevod(velikost):
    slovo = od_uzivatele
    nove = ""
    index = 0

    for i in slovo:
        index = 0

        if i in mala and velikost == 1:
            for a in mala:
                if a == i:
                    break
                index += 1
            nove += velka[index]
            index = 0

        elif i in velka and velikost == 0:
            for a in velka:
                if a == i:
                    break
                index += 1
            nove += mala[index]
            index = 0

        else:
            nove += i
        
    return nove
    
while True:
    print(Prevod(0),"--" ,  Prevod(1))




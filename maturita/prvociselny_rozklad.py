def prvociselny_rozklad(n):
    puvodni = n
    delitel = 2
    vysledek = ""
    while delitel <= puvodni // 2 and n > 1:
        if n % delitel == 0:
            n /= delitel
            if vysledek != "":
                vysledek += "*"
            vysledek += str(delitel)
            delitel = 2
        else:
            delitel += 1

    if vysledek == "":
        return n
    return vysledek

print(prvociselny_rozklad(12))    # → '2*2*3'""
print(prvociselny_rozklad(28))    # → '2*2*7'
print(prvociselny_rozklad(17))    # → '17'
print(prvociselny_rozklad(100))   # → '2*2*5*5'
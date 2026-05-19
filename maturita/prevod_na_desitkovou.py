def prevod_na_desitkovou(cislo, soustava):
    vysledek = 0
    mocnina = len(str(cislo)) - 1
    for i in str(cislo):
        vysledek += int(i)*soustava**mocnina
        mocnina -= 1
    return vysledek

print(prevod_na_desitkovou(2534, 6)+prevod_na_desitkovou(2244, 6))
def citac_slov(slova):
    vysledek = {}
    pocet = 0

    for i in range(len(slova)):
        if slova[i] not in vysledek:
            vysledek[slova[i]] = 1
        else:
            vysledek[slova[i]] += 1

    return vysledek


print(citac_slov(['jablko', 'hruška', 'jablko']))
# → {'jablko': 2, 'hruška': 1}

print(citac_slov(['a', 'b', 'a', 'c', 'b', 'a']))
# → {'a': 3, 'b': 2, 'c': 1}

print(citac_slov([]))
# → {}
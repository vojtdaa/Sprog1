def skupinovani(lst):
    vysledek = {}
    for i in lst:
        if i[0] not in vysledek:
            vysledek[i[0]] = [i]
        else: 
            vysledek[i[0]].append(i)
    
    return vysledek

print(skupinovani(['Adam', 'Bára', 'Anna', 'Cyril']))
# → {'A': ['Adam', 'Anna'], 'B': ['Bára'], 'C': ['Cyril']}

print(skupinovani(['Adam', 'Aleš', 'Anežka']))
# → {'A': ['Adam', 'Aleš', 'Anežka']}

print(skupinovani([]))
# → {}
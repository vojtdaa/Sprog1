def inverze_slovniku(slovnik):
    novy = {} 

    for klic in slovnik:
        novy[slovnik[klic]] = klic
        
    return novy


print(inverze_slovniku({'a': 1, 'b': 2, 'c': 3}))
# → {1: 'a', 2: 'b', 3: 'c'}

print(inverze_slovniku({'cs': 'čeština', 'en': 'angličtina'}))
# → {'čeština': 'cs', 'angličtina': 'en'}

print(inverze_slovniku({}))
# → {}
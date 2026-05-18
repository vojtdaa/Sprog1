def slouceni_bez_prepisu(a, b):
    vysledek = a

    for i in b:
        if i not in vysledek:
            vysledek[i] = b[i]
    
    return vysledek

print(slouceni_bez_prepisu({'a': 1, 'b': 2}, {'b': 99, 'c': 3}))
# → {'a': 1, 'b': 2, 'c': 3}

print(slouceni_bez_prepisu({}, {'a': 1, 'b': 2}))
# → {'a': 1, 'b': 2}

print(slouceni_bez_prepisu({'a': 1, 'b': 2}, {'a': 99, 'b': 99}))
# → {'a': 1, 'b': 2}
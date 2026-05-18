def frekvence_znaku(text):
    text = text.lower()
    vysledek = {}

    for pismeno in text:
        if pismeno != " ":
            if pismeno not in vysledek:
                vysledek[pismeno] = 1
            else:
                vysledek[pismeno] += 1
    return vysledek


print(frekvence_znaku('hello'))
# → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(frekvence_znaku('Hello World'))
# → {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

print(frekvence_znaku(''))
# → {}
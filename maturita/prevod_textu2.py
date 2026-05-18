mala_pismena = "abcdefghijklmnopqrstuvqxyz"
velka_pismena = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def prevod_textu(slovo, rezim):
    vysledek = ""
    index = 0

    if rezim == "mala":
        for i in range(len(slovo)):
            if slovo[i] not in mala_pismena:
                for x in velka_pismena:
                    if x == slovo[i]:
                        vysledek += mala_pismena[index]
                    index += 1
                index = 0
            else:
                vysledek += slovo[i]

    if rezim == "velka":
        for i in range(len(slovo)):
            if slovo[i] not in velka_pismena:
                for x in mala_pismena:
                    if x == slovo[i]:
                        vysledek += velka_pismena[index]
                    index += 1
                index = 0
            else:
                vysledek += slovo[i]

    return vysledek


print(prevod_textu('Python', 'velka'))   # → 'PYTHON'
print(prevod_textu('Python', 'mala'))    # → 'python'
print(prevod_textu('HeLLo', 'velka'))    # → 'HELLO'
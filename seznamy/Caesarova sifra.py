text = str(input("Napis slovo: "))
klic = int(input("Zadej posun: "))

rada = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

zasifrovan_text = ""

# zasifrovani

for znak in text:
    if znak in rada:
        for i in range(len(rada)):
            if znak == rada[i]:
                novy_znak = rada[(i+klic)%len(rada)]
                zasifrovan_text += novy_znak

print(zasifrovan_text)

# desifrovani
desifrovany_text = ""
for znak in zasifrovan_text:
    if znak in rada:
        for i in range(len(rada)):
            if znak == rada[i]:
                novy_znak = rada[i-klic%len(rada)]
                desifrovany_text += novy_znak

print(desifrovany_text)

print(ord("a"))
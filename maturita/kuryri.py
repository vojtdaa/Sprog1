def analyza_kuryru(data_balicku):
    vysledek = {}
    
    for i in range(len(data_balicku)):
        if data_balicku[i][0] not in vysledek:
            vysledek[data_balicku[i][0]] = {"pocet": 1, "celkova_vaha": data_balicku[i][2]}
        else:
            vysledek[data_balicku[i][0]]["pocet"] += 1
            vysledek[data_balicku[i][0]]["celkova_vaha"] += data_balicku[i][2]
    
    return vysledek


# --- TESTOVACÍ DATA ---
denni_prehled = [
    ['Petr', 'BAL101', 2.5],
    ['Jana', 'BAL102', 10.0],
    ['Petr', 'BAL103', 1.2],
    ['Karel', 'BAL104', 15.6],
    ['Jana', 'BAL105', 4.3],
    ['Petr', 'BAL106', 5.0]
]

# Spuštění funkce
vysledna_statistika = analyza_kuryru(denni_prehled)
print("Tvoje statistika kurýrů:\n", vysledna_statistika)

# --- OČEKÁVANÝ VÝSTUP (TEST) ---
# Petr doručil 3 balíčky o vahách 2.5 + 1.2 + 5.0 = 8.7 kg
# Jana doručila 2 balíčky o vahách 10.0 + 4.3 = 14.3 kg
# Karel doručil 1 balíček o váze 15.6 kg

ocekavany_vysledek = {
    'Petr': {'pocet': 3, 'celkova_vaha': 8.7},
    'Jana': {'pocet': 2, 'celkova_vaha': 14.3},
    'Karel': {'pocet': 1, 'celkova_vaha': 15.6}
}

print("\nVýsledek testu:")
# Používáme round(), protože Python může u desetinných čísel udělat drobnou nepřesnost (např. 8.70000000004)
# Tento test bezpečně ověří správnost dat struktury.
povedlo_se = True
for kuryr, data in ocekavany_vysledek.items():
    if kuryr not in vysledna_statistika:
        povedlo_se = False
        break
    tvoje_data = vysledna_statistika[kuryr]
    if tvoje_data.get('pocet') != data['pocet'] or round(tvoje_data.get('celkova_vaha', 0), 1) != data['celkova_vaha']:
        povedlo_se = False

if povedlo_se and len(vysledna_statistika) == len(ocekavany_vysledek):
    print("🎉 Dokonalé! Zvládl jsi i vnořené slovníky. Jsi připraven na složité datové struktury!")
else:
    print("❌ Výstup ještě neodpovídá zadání. Zkontroluj, jestli správně vytváříš a plníš vnořené slovníky.")
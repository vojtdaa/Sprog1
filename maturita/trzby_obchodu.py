def spocti_trzby_kategorii(seznam_prodeju):
    vysledek = {}
    
    for i in range(len(seznam_prodeju)):
        if seznam_prodeju[i][0] not in vysledek:
            vysledek[seznam_prodeju[i][0]] = seznam_prodeju[i][2]
        else:
            vysledek[seznam_prodeju[i][0]] += seznam_prodeju[i][2]
    
    return vysledek


# --- TESTOVACÍ DATA ---
prodeje_za_dnesek = [
    ['Elektro', 'Mobilní telefon', 12000],
    ['Knihy', 'Sci-fi román', 350],
    ['Elektro', 'Nabíječka', 500],
    ['Oblečení', 'Tričko', 400],
    ['Knihy', 'Detektivka', 400],
    ['Oblečení', 'Zimní bunda', 2500]
]

# Spuštění funkce
trzby = spocti_trzby_kategorii(prodeje_za_dnesek)
print("Tvoje tržby:", trzby)

# --- OČEKÁVANÝ VÝSTUP (TEST) ---
# Elektro: 12000 + 500 = 12500
# Knihy: 350 + 400 = 750
# Oblečení: 400 + 2500 = 2900

ocekavane_trzby = {
    'Elektro': 12500,
    'Knihy': 750,
    'Oblečení': 2900
}

print("\nVýsledek testu:")
if trzby == ocekavane_trzby:
    print("🎉 Skvělá práce! E-shop funguje bezchybně.")
else:
    print("❌ Částky nesouhlasí, zkus zkontrolovat sčítání v podmínce.")
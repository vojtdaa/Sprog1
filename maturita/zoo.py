def rozrad_zvirata(seznam_zvirat):
    vysledek = {}
    
    for i in range(len(seznam_zvirat)):
        if seznam_zvirat[i][1] not in vysledek:
            vysledek[seznam_zvirat[i][1]] = [seznam_zvirat[i][0]]
        else:
            vysledek[seznam_zvirat[i][1]].append(seznam_zvirat[i][0])
    
    return vysledek


# --- TESTOVACÍ DATA ---
vstupni_seznam = [
    ('Tučňák', 'led'),
    ('Lev', 'savana'),
    ('Lední medvěd', 'led'),
    ('Zebra', 'savana'),
    ('Delfín', 'voda')
]

# Spuštění funkce
zoo_safari = rozrad_zvirata(vstupni_seznam)
print(zoo_safari)

# --- OČEKÁVANÝ VÝSTUP (TEST) ---
# Funkce musí vrátit přesně tento slovník:
# {
#     'led': ['Tučňák', 'Lední medvěd'],
#     'savana': ['Lev', 'Zebra'],
#     'voda': ['Delfín']
# }

# Automatická kontrola, zda to máš správně:
ocekavany_vysledek = {
    'led': ['Tučňák', 'Lední medvěd'],
    'savana': ['Lev', 'Zebra'],
    'voda': ['Delfín']
}

print("\nVýsledek testu:")
if zoo_safari == ocekavany_vysledek:
    print("🎉 Skvělé! Funguje to dokonale.")
else:
    print("❌ Ještě to úplně nesedí, zkus to upravit.")
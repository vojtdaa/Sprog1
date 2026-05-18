def nejlepsi_student(evidence):
    prumery_zaku = {}
    for zak in evidence:
        prumery_zaku[zak] = sum(evidence[zak]["znamky"])/len(evidence[zak]["znamky"])

    nejlepsi = next(iter(prumery_zaku))

    for zak in prumery_zaku:
        if prumery_zaku[zak] < prumery_zaku[nejlepsi]:
            nejlepsi = zak
        elif prumery_zaku[zak] == prumery_zaku[nejlepsi]:
            if zak < nejlepsi:
                nejlepsi = zak

    return nejlepsi


evidence1 = {'Adam': {'znamky': [1, 2, 1]}, 'Bára': {'znamky': [3, 4, 3]}}
print(nejlepsi_student(evidence1))   # → 'Adam'

evidence2 = {'Zuzana': {'znamky': [2, 2, 2]}, 'Adam': {'znamky': [2, 2, 2]}}
print(nejlepsi_student(evidence2))   # → 'Adam'  (remíza → abecedně první)

# Test 3: Klasická situace (různé průměry, vyhrává jasně nejlepší)
evidence3 = {
    'Cyril': {'znamky': [3, 4, 5]},  # Průměr 4.0
    'Daniel': {'znamky': [1, 1, 2]}, # Průměr 1.33 -> NEJLEPŠÍ
    'Eva': {'znamky': [2, 3, 2]}     # Průměr 2.33
}
print("Test 3 (Jasný vítěz):", "OK" if nejlepsi_student(evidence3) == 'Daniel' else "CHYBA (čekalo se 'Daniel')")


# Test 4: Remíza tří studentů se stejným průměrem (rozhoduje abeceda)
evidence4 = {
    'Cyril': {'znamky': [2, 2, 2]},  # Průměr 2.0
    'Bára': {'znamky': [2, 2, 2]},   # Průměr 2.0 -> NEJLEPŠÍ (abecedně první)
    'Daniel': {'znamky': [2, 2, 2]}  # Průměr 2.0
}
print("Test 4 (Remíza 3 lidí):", "OK" if nejlepsi_student(evidence4) == 'Bára' else "CHYBA (čekalo se 'Bára')")


# Test 5: Jenom jeden student v evidenci
evidence5 = {
    'Osvald': {'znamky': [5, 5, 4]}  # Průměr nic moc, ale je sám
}
print("Test 5 (Jeden student):", "OK" if nejlepsi_student(evidence5) == 'Osvald' else "CHYBA (čekalo se 'Osvald')")


# Test 6: Složitější remíza (dva nejlepší mají stejný průměr, ostatní jsou horší)
evidence6 = {
    'Filip': {'znamky': [1, 2]},     # Průměr 1.5 -> NEJLEPŠÍ (před Honzou)
    'Hana': {'znamky': [4, 4]},      # Průměr 4.0
    'Honza': {'znamky': [1, 2]},     # Průměr 1.5
    'Ivan': {'znamky': [3, 2]}       # Průměr 2.5
}
print("Test 6 (Remíza na čele):", "OK" if nejlepsi_student(evidence6) == 'Filip' else "CHYBA (čekalo se 'Filip')")


# Test 7: Různý počet známek (kdo má méně známek, může mít lepší průměr)
evidence7 = {
    'Monika': {'znamky': [1]},          # Průměr 1.0 -> NEJLEPŠÍ
    'Nikola': {'znamky': [1, 2, 1, 1]}  # Průměr 1.25
}
print("Test 7 (Různý počet známek):", "OK" if nejlepsi_student(evidence7) == 'Monika' else "CHYBA (čekalo se 'Monika')")
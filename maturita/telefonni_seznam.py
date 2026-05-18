def telefonni_seznam(kontakty, jmeno):

    if jmeno not in kontakty:
        return "Kontak nenalezen"
    
    else:
        return kontakty[jmeno]
    


kontakty = {'Adam': '777 111 222', 'Bára': '777 333 444'}
print(telefonni_seznam(kontakty, 'Adam'))    # → '777 111 222'
print(telefonni_seznam(kontakty, 'Cyril'))   # → 'Kontakt nenalezen'
print(telefonni_seznam({}, 'Adam'))          # → 'Kontakt nenalezen'
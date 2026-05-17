def urci_kategorii(vek):
    dite = 12
    mladistvy = 17
    dospely = 64
    senior = 65
    if vek < 0:
        return "Nelze urcit ze zaporne hodnoty"
    
    if vek <= dite:
        return "dite"
    
    elif vek <= mladistvy:
        return "mladistvy"
    
    elif vek <= dospely:
        return "dospely"
    
    elif vek >= senior:
        return "senior"
    
    else:
        return "Nelze urcit"
    
print(urci_kategorii(-5))    # → 'Dítě'
print(urci_kategorii(15))   # → 'Mladistvý'
print(urci_kategorii(25))   # → 'Dospělý'
print(urci_kategorii(70))   # → 'Senior'
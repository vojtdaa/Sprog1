def urc_kvadrant(x,y):
    if x == 0 and y == 0:
        return "pocatek"
    if x == 0 or y == 0:
        return "bod lezi mezi kvadranty"
 
    if x > 0:
        if y > 0:
            return 1
        if y < 0:
            return 4
    if x < 0:
        if y > 0:
            return 2
        if y < 0:
            return 3

print(urc_kvadrant(5, 3))    # → 1
print(urc_kvadrant(-4, 7))   # → 2
print(urc_kvadrant(-3, -1))  # → 3
print(urc_kvadrant(2, -5))   # → 4
print(urc_kvadrant(0, 0))    # → 'pocatek'
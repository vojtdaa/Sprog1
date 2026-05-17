def typ_trojuhelniku(a, b, c):
    if a == b == c:
        return "rovnostranny"
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "pravouhly" 

    if a == b or a == c or b == c:
        return "rovnoramenny"
    
    elif a > 0 and b > 0 and c > 0:
        return "ruznostranny"
    else:
        return None
    
print(typ_trojuhelniku(5, 5, 5))   # → 'rovnostranný'
print(typ_trojuhelniku(3, 4, 5))   # → 'pravoúhlý'
print(typ_trojuhelniku(5, 5, 8))   # → 'rovnoramenný'
print(typ_trojuhelniku(3, 4, 6))   # → 'různostranný'
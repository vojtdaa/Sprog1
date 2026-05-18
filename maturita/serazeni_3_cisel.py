def serad_sestupne(a, b, c):
    if a >= c and a >= b:
        if b > c:
            return [a, b, c]
        else:
            return [a, c, b]
        
    if c >= a and c >= b:
        if a > b:
            return [c, a, b]
        else: [c, b, a]
    
    if b >= a and b >= c:
        if a > c:
            return [b, a, c]
        else:
            return [b, c, a]
    else:
        return [a, b, c]

print(serad_sestupne(1, 5, 2))
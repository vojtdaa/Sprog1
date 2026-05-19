def odmocnina(n):
    x = 0
    y = 0
    i = 0
    j = 0

    while True:
        if i**2 < n and (i+1)**2 > n:
            x = i
        if j**2 > n:
            y = j
            break
        i += 1
        j += 1

    def najdi_stred(n, x, y):
        stred = (x+y)/2

        if round(stred**2, 4) == n:
            return round(stred, 4)
        
        if stred**2 > n:
            return najdi_stred(n, x, stred)
        
        if stred**2 < n:
            return najdi_stred(n, stred, y)
    
    return najdi_stred(n, x, y)

print(odmocnina(4))   # → ≈ 2.0
print(odmocnina(2))   # → ≈ 1.4142
print(odmocnina(9))   # → ≈ 3.0
print(odmocnina(16))   # → ≈ 4.0
print(odmocnina(225))   # → ≈ 15
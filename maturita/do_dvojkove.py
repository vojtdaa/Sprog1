def do_dvojkove(n):
    vysledek = ""
    if n == 0:
        return 0
    while n > 0:
        vysledek = str(n % 2) + vysledek
        n //= 2
    return vysledek

print(do_dvojkove(0))    # → '0'
print(do_dvojkove(5))    # → '101'
print(do_dvojkove(10))   # → '1010'
print(do_dvojkove(255))  # → '11111111'

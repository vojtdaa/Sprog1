def je_trojuhelnik(a, b, c):
    if a + b > c and a + c > b and c + b > c:
        return True
    return False

print(je_trojuhelnik(3, 4, 5))    # → True
print(je_trojuhelnik(1, 2, 10))   # → False
print(je_trojuhelnik(5, 5, 5))    # → True
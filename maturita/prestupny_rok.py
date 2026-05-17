def je_prestupny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        return True
    return False

print(je_prestupny(2024))   # → True
print(je_prestupny(1900))   # → False
print(je_prestupny(2000))   # → True
print(je_prestupny(2023))   # → False
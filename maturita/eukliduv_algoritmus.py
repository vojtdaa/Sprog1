def nsd(a, b):

    if a < b:
        a, b = b, a

    if a % b == 0:
        return b
    return nsd(b, a % b)

print(nsd(5, 10))     # → 5
print(nsd(48, 18))    # → 6
print(nsd(100, 75))   # → 25
print(nsd(17, 13))    # → 1
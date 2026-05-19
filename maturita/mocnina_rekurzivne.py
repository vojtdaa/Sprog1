def mocnina(a, x):
    if x == 0:
        return 1
    
    return a*mocnina(a, x-1)

print(mocnina(2, 0))    # → 1
print(mocnina(2, 10))   # → 1024
print(mocnina(3, 4))    # → 81
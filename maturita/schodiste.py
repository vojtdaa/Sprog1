def schodiste(n):

    def jdi(n, schod):
        if schod == n:
            return 1
        if schod > n:
            return 0
        
        return jdi(n, schod+1) + jdi(n, schod+2)
    
    return jdi(n, 0)

print(schodiste(1))   # → 1
print(schodiste(2))   # → 2
print(schodiste(3))   # → 3
print(schodiste(5))   # → 8
print()

def schodiste2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return schodiste2(n-1) + schodiste(n-2)

print(schodiste2(1))   # → 1
print(schodiste2(2))   # → 2
print(schodiste2(3))   # → 3
print(schodiste2(5))   # → 8
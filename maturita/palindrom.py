def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrom(s[1:-1])
    
    else: return False

print(palindrom('radar'))   # → True
print(palindrom('kayak'))   # → True
print(palindrom('ahoj'))    # → False
print(palindrom('a'))       # → True

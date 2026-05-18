def Zjisti(a):
    if a == 1:
        return False
    if a == 2:
        return True
    
    for i in range(2, a//2+1):
        if a % i == 0:
            return False
        else: return True
        
print(Zjisti(1))
print(Zjisti(2))
print(Zjisti(8))
print(Zjisti(10))
print(Zjisti(11))
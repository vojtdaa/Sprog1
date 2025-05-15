def fact(n):
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    if n > 0: 
        return n*fact(n-1)
    
    else : return None

print(fact(-3))
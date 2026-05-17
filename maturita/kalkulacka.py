def Kalkulacka(a, b, op):

    if op == "+":
        return a + b
    
    elif op == "-":
        return a - b
    
    elif op == ":" or op == "/":
        if b == 0:
            return "Nelze delit nulou."

        return a / b
    
    elif op == "x" or op == "*" or op ==".":
        return a* b
    else:
        return "Neznama operace."
    

print(Kalkulacka(10, 3, '-'))  
print(Kalkulacka(6, 7, '*'))    
print(Kalkulacka(20, 4, '/')) 
print(Kalkulacka(10, 5, '+'))  
print(Kalkulacka(10, 0, '/'))   
print(Kalkulacka(10, 5, '%'))  

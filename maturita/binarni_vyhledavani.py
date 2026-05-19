def binarni_vyhledavani(lst, cil):
    if not lst:
        return False
    prostredni_index = len(lst)//2
    if lst[prostredni_index] == cil:
        return True
    
    if lst[prostredni_index] < cil:
        return binarni_vyhledavani(lst[prostredni_index:len(lst)-1], cil)
    else:
        return binarni_vyhledavani(lst[0:prostredni_index], cil)
    
print(binarni_vyhledavani([1, 3, 5, 7, 9], 5))   # → True
print(binarni_vyhledavani([1, 3, 5, 7, 9], 4))   # → False
print(binarni_vyhledavani([], 5))                 # → False

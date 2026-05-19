def soucet_rekurzivne(lst):
    soucet = 0

    def scitej(lst, soucet):
        if not lst:
            return soucet
        soucet += lst[0]

        return scitej(lst[1:], soucet)
    
    return scitej(lst, soucet)

print(soucet_rekurzivne([1, 2, 3]))       # → 6
print(soucet_rekurzivne([5]))             # → 5
print(soucet_rekurzivne([1, 2, 3, 4, 5])) # → 15
print(soucet_rekurzivne([]))              # → 0
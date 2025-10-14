

def ApproximatePi(steps = 1000):
    vysledek = 0
    znamenko = 1
    for i in range(1, steps+1, 2):
        vysledek += 4*znamenko*(1/i)
        znamenko = -znamenko
    return vysledek 

print(ApproximatePi())

def BBPFormula(steps = 1000):
    vysledek = 0
    for k in range(steps):
        vysledek += ((1/(16**k))*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6))))
    return vysledek

print(BBPFormula())

print(ApproximatePi()-BBPFormula())
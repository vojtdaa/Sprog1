moznosti = ["kámen", "nůžky", "papír"]

def kamen_nuzky_papir(hrac1, hrac2):
    if hrac1 == "kámen":
        if hrac2 == "kámen":
            return "remíza"
        elif hrac2 == "nůžky":
            return "hrac1"
        elif hrac2 == "papír":
            return "hrac2"
    
    elif hrac1 == "nůžky":
        if hrac2 == "kámen":
            return "hrac2"
        elif hrac2 == "nůžky":
            return "remíza"
        elif hrac2 == "papír":
            return "hrac1"
        
    elif hrac1 == "papír":
        if hrac2 == "kámen":
            return "hrac1"
        elif hrac2 == "nůžky":
            return "hrac2"
        elif hrac2 == "papír":
            return "remíza"
    return

print(kamen_nuzky_papir("nůžky", "kámen"))
print(kamen_nuzky_papir("papír", "kámen"))
print(kamen_nuzky_papir("papír", "nůžky"))
print(kamen_nuzky_papir("papír", "papír"))
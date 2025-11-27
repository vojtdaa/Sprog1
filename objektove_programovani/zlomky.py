import math

class Zlomek:
    def __init__(self, citatel, jmenovatel = 1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel
        pass

    def __str__(self):
        return str(self.citatel) + "/" + str(self.jmenovatel)

    def zkrat(self):
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        self.citatel //= nsd
        self.jmenovatel //= nsd
        return self
    
    
    def __add__(self, jiny):
        vysledny_citatel = self.citatel*jiny.jmenovatel + self.jmenovatel*jiny.citatel
        vysledny_jmenovatel = self.jmenovatel*jiny.jmenovatel

        vysledek = Zlomek(vysledny_citatel, vysledny_jmenovatel)
        
        return vysledek.zkrat()
    
    def __sub__(self, jiny):
        vysledny_citatel = self.citatel*jiny.jmenovatel - self.jmenovatel*jiny.citatel
        vysledny_jmenovatel = self.jmenovatel*jiny.jmenovatel

        vysledek = Zlomek(vysledny_citatel, vysledny_jmenovatel)
        
        return vysledek.zkrat()

    def __mul__(self, jiny):
        vysledny_citatel = self.citatel*jiny.citatel
        vysledny_jmenovatel = self.jmenovatel*jiny.jmenovatel

        vysledek = Zlomek(vysledny_citatel, vysledny_jmenovatel)

        return vysledek.zkrat()
    
    def __truediv__(self, jiny):
        vysledny_citatel = self.citatel*jiny.jmenovatel
        vysledny_jmenovatel = self.jmenovatel*jiny.citatel

        vysledek = Zlomek(vysledny_citatel, vysledny_jmenovatel)

        return vysledek.zkrat()
        
    def __eq__(self, jiny):
        novy_zlomek1 = Zlomek(self.citatel*jiny.jmenovatel, self.jmenovatel*jiny.jmenovatel)
        novy_zlomek2 = Zlomek(jiny.citatel*self.jmenovatel, jiny.jmenovatel*self.jmenovatel)
        if (novy_zlomek1.citatel == novy_zlomek2.citatel):
            return True
        else: return False


# Test 1: Vytvoření zlomků
z1 = Zlomek(1, 2)
z2 = Zlomek(2, 4)
z3 = Zlomek(5)
print(f"z1 = {z1}")  # 1/2
print(f"z2 = {z2}")  # 3/4
print(f"z3 = {z3}")  # 5/1
# Test 2: Sčítání
print(f"{z1} + {z2} = {z1 + z2}")  # 5/4
# Test 3: Odčítání
print(f"{z2} - {z1} = {z2 - z1}")  # 1/4
# Test 4: Násobení
print(f"{z1} * {z2} = {z1 * z2}")  # 3/8
# Test 5: Dělení
print(f"{z1} / {z2} = {z1 / z2}")  # 2/3
# Test 6: Složitější výpočet
print(f"({z1} + {z2}) * {z3} = {(z1 + z2) * z3}")  # 25/4
# Test 7: Zkracování
z4 = Zlomek(8, 12)
print(f"Před zkrácením: {z4}")  # 8/12
z4.zkrat()
print(f"Po zkrácení: {z4}")    # 2/3

if z1 == z2:
    print("rovnaji se")
else: print("nerovnaji se")
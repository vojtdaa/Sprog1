class Zlomek:
    def __init__(self, citatel, jmenovatel):
        self.citatel = citatel
        self.jmenovatel = jmenovatel

    def __str__(self):
        return f"{self.citatel} / {self.jmenovatel}"
        
    def __add__(self, druhy_zlomek):
        vysledny_citatel = self.citatel*druhy_zlomek.jmenovatel + self.jmenovatel*druhy_zlomek.citatel
        vysledny_jmenovatel = self.jmenovatel*druhy_zlomek.jmenovatel

        vysledek = Zlomek(vysledny_citatel, vysledny_jmenovatel)
        return vysledek
    
    def __sub__(self, druhy_zlomek):
        vysledek = Zlomek(self.citatel*druhy_zlomek.jmenovatel - self.jmenovatel*druhy_zlomek.citatel, self.jmenovatel*druhy_zlomek.jmenovatel)
        return vysledek

    def __mul__(self, druhy_zlomek):
        vysledek = Zlomek(self.citatel*druhy_zlomek.citatel, self.jmenovatel*druhy_zlomek.jmenovatel)
        return vysledek
    
    def __truediv__(self, druhy_zlomek):
        vysledek = Zlomek(self.citatel*druhy_zlomek.jmenovatel, self.jmenovatel*druhy_zlomek.citatel)
        return vysledek
    
zlomek = Zlomek(1, 2)
zlomek2 = Zlomek(1, 4)

print(zlomek / zlomek2)
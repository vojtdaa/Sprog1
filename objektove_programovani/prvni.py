class Hrac:
    #konstruktor
    def __init__(self, name):  
        #atributy
        self.jmeno = name
        self.zivoty = 100
        self.__penize = 20
    

    #metody
    def utrzi_zraneni(self, dmg):
        self.__penize = self.__penize + 20
        self.zivoty -= dmg

    def zjisti_penize(self):
        return self.__penize

hrac1 = Hrac("David")
hrac1.utrzi_zraneni(20)
print(hrac1.zjisti_penize())

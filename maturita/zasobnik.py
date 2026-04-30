class Prvek:
    def __init__(self, hodnota, predchozi):
        self.hodnota = hodnota
        self.predchozi = predchozi

class Zasobnik:
    def __init__(self, peak = None):
        self.peak = peak

    def novy_prvek(self, hodnota):
        novy = Prvek(hodnota, self.peak)
        self.peak = novy
        return self.peak
    
    def peak(self):
        return self.peak


print(Zasobnik.novy_prvek())
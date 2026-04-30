class Prvek:
    def __init__(self, hodnota, predchozi = None):
        self.hodnota = hodnota
        self.predchozi = predchozi

class Zasobnik:
    def __init__(self, peak = None, last = None):
        self.peak = peak

    def __novy_prvek__(self, hodnota):
        novy_prvek = Prvek(hodnota)
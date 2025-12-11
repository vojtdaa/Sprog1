class Barva:

    def __init__(self, r, g, b):
        if r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
            return ValueError
        
        self.red = r
        self.green = g
        self.blue = b
        
        pass

    def __str__(self):
        return str(f"RGB({self.red}, {self.green}, {self.blue})")
    
    def __add__(self, jina):
        new_r = (self.red + jina.red)/2
        new_g = (self.green + jina.green)/2
        new_b = (self.blue + jina.blue)/2
        return Barva(new_r, new_g, new_b)
    
    def __mul__(self, nasobek):
        new_r = int(self.red * nasobek)
        if new_r > 255:
            new_r = 255

        new_g = int(self.green * nasobek)
        if new_g > 255:
            new_g = 255
        new_b = int(self.blue * nasobek)
        if new_b > 255:
            new_b = 255
        return Barva(new_r, new_g, new_b)
    
    def invertuj(self):
        new_r = 255 - self.red
        new_g = 255 - self.green
        new_b = 255 - self.blue
        return Barva(new_r, new_g, new_b)
    
    def to_hex(self):
        zacatek = ""
        stred = ""
        konec = ""


        new_r = hex(self.red)
        if len(new_r) == 4:
            new_r = new_r[2] + new_r[3]
        else: new_r = "0" + new_r[2]
        new_g = hex(self.green)
        new_b = hex(self.blue)
        vysledek = f"#{new_r} {new_g} {new_b}"
        return vysledek


cervena = Barva(255, 5, 0)
modra = Barva(0, 0, 255)
print("michat muzes pouze 2 barvy\n")
print(str(cervena))
print(cervena + modra)

print("nasobek: ", end="")
print(cervena * 0.1)

print("inverze: ", end="")
print(cervena.invertuj())


print(f"to hex: {cervena.to_hex()}")
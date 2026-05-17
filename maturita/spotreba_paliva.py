vzdalenost = float(input("Zadej vzdálenost: "))
spotreba = float(input("Zadej spotrebu [l/100km]: "))
cena = float(input("Zadej cenu plaiva [Kč/l]: "))

palivo = vzdalenost*(spotreba/100)

print(f"Palivo: {round(palivo, 2)} l, Cena: {round(palivo*cena, 2)} Kč")
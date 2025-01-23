import math

strana1 = float(input("Zadej délku první strany: "))
strana2 = float(input("Zadej délku druhé strany: "))
strana3 = float(input("Zadej délku třetí strany: "))

je_trojuhelnik = False

if strana1 + strana2 > strana3 and strana1 + strana3 > strana2 and strana2 + strana3 > strana1:
    if strana1 > 0 and strana2 > 0 and strana3 > 0:
        je_trojuhelnik = True
else:
    print(f"Strany {strana1}, {strana2}, {strana3} netvoří trojúhelník.")
    exit()

if je_trojuhelnik:

    if strana1 == strana2 == strana3:
        print(f"Strany {strana1}, {strana2}, {strana3} tvoří rovnostranný trojúhelník.")

    elif strana1 == strana2 or strana2 == strana3 or strana1 == strana3:
        print(f"Strany {strana1}, {strana2}, {strana3} tvoří rovnoramenný trojúhelník.")

    else:
        print(f"Strany {strana1}, {strana2}, {strana3} tvoří obecný trojúhelník.")

mensi2 = float
mensi1 = float

nejvetsi = strana1
if strana2 > strana1:
    nejvetsi = strana2
if strana3 > strana1 and strana3 > strana2:
    nejvetsi = strana3

if nejvetsi == strana1:
    mensi1 = strana2
    mensi2 = strana3
elif nejvetsi == strana2:
    mensi1 = strana1
    mensi2 = strana3
elif nejvetsi == strana3:
    mensi1 = strana2
    mensi2 = strana1

if nejvetsi **2 == (mensi2 **2 + mensi1 **2):
    print("pravouhly")
elif nejvetsi **2 > (mensi2 **2 + mensi1 **2):
    print("tupouhly")
else:
    print("ostrouhly")

vzdalenost = float(input("Zadej vzdalenost [m]: "))
cas = float(input("Zadej čas [s]: "))

if cas < 0:
    cas = cas * -1

rychlost = vzdalenost / cas

print(f"{rychlost} m/s")

rychlost2 = rychlost * 3.6

print(f"{rychlost2} km/h")
print(-rychlost2)
while True:
    cislo = int(input("Zadej cislo: "))

    pocet_delitelu = 0

    for i in range(1, cislo//2):
        if cislo % i == 0:
            pocet_delitelu += 1

    if pocet_delitelu == 2 and cislo > 0:
        print("Je prvocislo")
    else: 
        print("Neni prvocislo")
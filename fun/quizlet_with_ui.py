import msvcrt
import tkinter as tk

with open("nemecka_slovicka_1.txt", "r", encoding="utf-8") as f:
    upload = f.read()

slova = []
definice = []

not_know_slova = []
not_know_definice = []
know_count = 0
not_know_count = 0


def SplitWords(slova, definice):
    pocket = ""
    for i in upload:
        if i == ";":
            slova.append(pocket)
            pocket = ""
        elif i == "*":
            definice.append(pocket)
            pocket = ""
        elif i == "$":
            break

        elif i == "\n":
            continue
        else:
            pocket += i
    return slova, definice

slova, definice = SplitWords(slova, definice)
ted_slov = len(slova)

def GetKey():
    while True:
        key = msvcrt.getch()
        vysledek = ""
        
        if key == b"\x1b":
            vysledek = "esc"
            return vysledek
    
        if key == b"\xe0":
            key2 = msvcrt.getch()
            if key2 == b"H" or key2 == b"P":
                vysledek = "flip"
                return vysledek
            elif key2 == b"M":
                vysledek = "know"
                return vysledek
            elif key2 == b"K":
                vysledek = "not know"
                return vysledek

def Play(slova, definice):
    global know_count
    global not_know_count
    know_count = 0
    not_know_count = 0

    not_know_slova = []
    not_know_definice = []

    for i in range(len(slova)):
        slovo = True
        while True:
            if slovo:
                print("\033[F\033[K", end="")
                print(slova[i])
            else:
                print("\033[F\033[K", end="")
                print(definice[i])
            
            a = GetKey()
            if a == "flip":
                slovo = not slovo
            elif a == "know":
                know_count += 1
                break
            elif a == "not know":
                not_know_slova.append(slova[i])
                not_know_definice.append(definice[i])
                not_know_count += 1
                break
            elif a == "esc":
                return not_know_slova, not_know_definice
    
    return not_know_slova, not_know_definice

#zacatek programu
res_x = 900
res_y = 500
res = str(res_x)+"x"+str(res_y)
okno = tk.Tk()        # 2️⃣ vytvoření hlavního okna
okno.title("Language cards")  
okno.geometry(res)  # šířka x výška v pixelech

slovicko = tk.Label(okno, text="das Auto", font=("Arial", 24))
slovicko.pack(pady=res_y/4.5)

not_know_but = tk.Button(okno, text="Don't know", width=15, height=2, command=lambda: print("Nevim"))
not_know_but.place(relx = 0.33, rely = 0.35)

know_but = tk.Button(okno, text="Know", width=15, height=2, command=lambda: print("Vim"))
know_but.place(relx=0.5, rely=0.35)

okno.mainloop()   

print("Ovladej sipkami (esc - konec)\n")
not_know_slova, not_know_definice = Play(slova, definice)

print("\nVysledek:")

not_know_percent = round(not_know_count/ted_slov*100, 2)
know_percent = round(know_count/ted_slov*100, 2)
ted_slov = not_know_count

if know_percent > 0:
    print(f"Znas \033[32m{know_percent}%\033[0m slov.")
if not_know_percent > 0:
    print(f"Neznas \033[31m{not_know_percent}%\033[0m slov.")

if know_percent == 100:
    print("\n\033[33mZnas vsechny\033[0m")
else:
    while True:
        if not_know_percent == 0:
            print("\n\033[33mZnas vsechny\033[0m")
            break

        print("\nPokracovat v uceni?")

        continue_playing = GetKey()

        if continue_playing != "esc" and not_know_percent>0:
            ted_slov = len(not_know_slova)
            if ted_slov == 0:
                print("\n\033[33mZnas vsechny\033[0m")
                break
            not_know_slova, not_know_definice = Play(not_know_slova, not_know_definice)
            


            print("\nVysledek:")

            not_know_percent = round((len(not_know_slova)/ted_slov)*100, 2)
            know_percent = round(100-not_know_percent, 2)
            if know_percent > 0:
                print(f"Znas \033[32m{know_percent}%\033[0m slov.")
            if not_know_percent > 0:
                print(f"Neznas \033[31m{not_know_percent}%\033[0m slov.")

        else: break








'''
print("\033[31mToto je červený text\033[0m") #\033[31m\033[0m
print("\033[32mToto je zelený text\033[0m") #\033[32m\033[0m
print("\033[33mToto je žlutý text\033[0m") #\033[33m\033[0m
print("\033[34mToto je modrý text\033[0m") #\033[34m\033[0m
'''
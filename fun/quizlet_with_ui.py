import tkinter as tk
import copy

with open("nemecka_slovicka_1.txt", "r", encoding="utf-8") as f:
    upload = f.read()

puvodni_slova = []
puvodni_definice = []

not_know_slova = []
not_know_definice = []
know_count = 0
not_know_count = 0
index = 1
flipped = False
ended = False


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

puvodni_slova, puvodni_definice = SplitWords(puvodni_slova, puvodni_definice)
slova = copy.deepcopy(puvodni_slova)
definice = copy.deepcopy(puvodni_definice)
ted_slov = len(slova)

#zacatek programu

def Know():
    global index
    global know_count
    global not_know_count
    know_count+=1

    if index == len(slova):
        if not_know_count == 0:
            End()
            score_right.config(text = f"Correct {know_count}")
            know_but.config(state="disabled")
            not_know_but.config(state="disabled")
            return
        else:
            repeat_but.place(relx=0.5, rely=0.7, anchor="center")
            score_right.config(text = f"Correct {know_count}")
            know_but.config(state="disabled")
            not_know_but.config(state="disabled")
            return
    LoadWord()
    score_right.config(text = f"Correct {know_count}")
   
    return

def NotKnow():
    global index
    global not_know_count
   
    not_know_slova.append(slova[index-1])
    not_know_definice.append(definice[index-1])
    not_know_count += 1

    score_wrong.config(text = f"Wrong {not_know_count}")

    if index == len(slova):
        not_know_but.config(state="disabled")
        know_but.config(state="disabled")
        repeat_but.place(relx=0.5, rely=0.7, anchor="center")
        return
    LoadWord()
    return

def LoadWord():
    global index
    global flipped
    flipped = False

    slovicko.config(text=slova[index])
    index += 1
    return

def Flip():
    global index
    global flipped
    flipped = not flipped
    if not ended:
        if flipped:
            slovicko.config(text=definice[index-1])
        else:
            slovicko.config(text=slova[index-1])
    return

def Repeat():
    global slova
    global definice
    global not_know_slova
    global not_know_definice
    global index
    global know_count
    global not_know_count

    slova = not_know_slova
    definice = not_know_definice
    not_know_slova = []
    not_know_definice = []
    index = 0
    know_count = 0
    not_know_count = 0
    LoadWord()
    repeat_but.place_forget()
    not_know_but.config(state="normal")
    know_but.config(state="normal")
    score_right.config(text = f"Correct {know_count}")
    score_wrong.config(text = f"Wrong {not_know_count}")
    return

def End():
    global ended
    ended = True
    repeat_but.place_forget()
    flip_but.config(state="disabled")
    slovicko.config(text="You know everything :)")
    restart_but.place(relx=0.1, rely=0.9, anchor="center")

def Restart():
    global slova
    global definice
    global not_know_slova
    global not_know_definice
    global index
    global know_count
    global not_know_count
    global puvodni_slova
    global puvodni_definice

    slova = copy.deepcopy(puvodni_slova)
    definice = copy.deepcopy(puvodni_definice)
    not_know_slova = []
    not_know_definice = []
    index = 0
    know_count = 0
    not_know_count = 0
    LoadWord()

    restart_but.place_forget()
    repeat_but.place_forget()
    not_know_but.config(state="normal")
    know_but.config(state="normal")
    score_right.config(text = f"Correct {know_count}")
    score_wrong.config(text = f"Wrong {not_know_count}")


res_x = 900
res_y = 500
res = str(res_x)+"x"+str(res_y)
okno = tk.Tk()        # 2️⃣ vytvoření hlavního okna
okno.title("Language cards")
okno.minsize(600, 400)  
okno.geometry(res)  # šířka x výška v pixelech

score_wrong = tk.Label(okno, text=f"Wrong {not_know_count}", font=("Arial", 18))
score_wrong.place(relx=0.05, rely=0.05)

score_right = tk.Label(okno, text=f"Correct {know_count}", font=("Arial", 18))
score_right.place(relx=0.8, rely=0.05)

slovicko = tk.Label(okno, text=slova[0], font=("Arial", 28, "bold"))
slovicko.place(relx=0.5, rely=0.4, anchor="center")

not_know_but = tk.Button(okno, text="Don't know", font=("Arial", 16), width=12, height=2, bg="#ff0d00", fg="black", command=NotKnow)
not_know_but.place(relx=0.25, rely=0.7, anchor="center")

know_but = tk.Button(okno, text="Know", font=("Arial", 16), width=12, height=2, bg="#00ff00", fg="black", command=Know)
know_but.place(relx=0.75, rely=0.7, anchor="center")

flip_but = tk.Button(okno, text="Flip", font=("Arial", 16), width=12, height=2, bg="#37b6ff", fg="black", command=Flip)
flip_but.place(relx=0.5, rely=0.7, anchor="center")

restart_but = tk.Button(okno, text="restart", font=("Arial", 10), width=6, height=1, bg="#000000", fg="white", command=Restart)

repeat_but = tk.Button(okno, text="Repeat", font=("Arial", 16), width=12, height=2, bg="#37b6ff", fg="black", command=Repeat)

okno.mainloop()   

'''
print("\033[31mToto je červený text\033[0m") #\033[31m\033[0m
print("\033[32mToto je zelený text\033[0m") #\033[32m\033[0m
print("\033[33mToto je žlutý text\033[0m") #\033[33m\033[0m
print("\033[34mToto je modrý text\033[0m") #\033[34m\033[0m
'''
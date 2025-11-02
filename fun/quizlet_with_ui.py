import tkinter as tk
import copy
import random
with open("words_given.txt", "r", encoding="utf-8") as f:
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
reverse = False

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

    if index == len(slova)-1:
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
    else: Next()
    score_right.config(text = f"Correct {know_count}")
   
    return

def NotKnow():
    global index
    global not_know_count
   
    not_know_slova.append(slova[index])
    not_know_definice.append(definice[index])
    not_know_count += 1

    score_wrong.config(text = f"Wrong {not_know_count}")

    if index == len(slova)-1:
        not_know_but.config(state="disabled")
        know_but.config(state="disabled")
        repeat_but.place(relx=0.5, rely=0.7, anchor="center")
        return
    
    Next()
    return

def Next():
    global index
    global flipped
    global reverse
    index += 1
    flipped = False
    shuffle_but.config(state="disabled")

    if reverse:
        LoadDefinition()
    else:
        LoadWord()
    return

def LoadWord():
    global index
    global flipped
    flipped = False

    slovicko.config(text=slova[index])
    return

def LoadDefinition():
    global index
    global flipped
    flipped = True

    slovicko.config(text=definice[index])
    return

def Flip():
    global index
    global flipped
    flipped = not flipped
    if flipped:
        LoadDefinition()
    else:
        LoadWord()
    return

def Repeat():
    global slova
    global definice
    global not_know_slova
    global not_know_definice
    global index
    global know_count
    global not_know_count
    global reverse

    slova = not_know_slova
    definice = not_know_definice
    not_know_slova = []
    not_know_definice = []
    index = 0
    know_count = 0
    not_know_count = 0
    if reverse:
        LoadDefinition()
    else:
        LoadWord()
    repeat_but.place_forget()
    EnableAll()
    score_right.config(text = f"Correct {know_count}")
    score_wrong.config(text = f"Wrong {not_know_count}")
    shuffle_but.config(state="normal")
    return

def End():
    global ended
    ended = True
    repeat_but.place_forget()
    DisableAll()
    slovicko.config(text="You know everything :)")
    return

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
    global reverse

    slova = copy.deepcopy(puvodni_slova)
    definice = copy.deepcopy(puvodni_definice)
        
    not_know_slova = []
    not_know_definice = []
    index = 0
    know_count = 0
    not_know_count = 0
    if reverse:
        LoadDefinition()
    else:
        LoadWord()

    repeat_but.place_forget()
    EnableAll()
    score_right.config(text = f"Correct {know_count}")
    score_wrong.config(text = f"Wrong {not_know_count}")
    shuffle_but.config(state="normal")
    return

def Reverse():
    global reverse
    global flipped
    reverse = not reverse
    if reverse:
        show.config(text="showing definition")
        if not flipped:
            Flip()
    else:
        show.config(text="showing word")
        if flipped:
            Flip() 
    return

def DisableAll():
    not_know_but.config(state="disabled")
    flip_but.config(state="disabled")
    know_but.config(state="disabled")
    reverse_but.config(state="disabled")
    return

def EnableAll():
    not_know_but.config(state="normal")
    flip_but.config(state="normal")
    know_but.config(state="normal")
    reverse_but.config(state="normal")
    return   

def Shuffle():
    global slova
    global definice
    global puvodni_slova
    global puvodni_definice
    global index
    global reverse
    global know_count
    global not_know_count
    if not_know_count > 0 or know_count > 0:
        return
    
    if len(slova) == 1:
        return
    
    possibles = [n for n in range(len(slova))]
    new_slova = []
    new_definice = []
    new_pos = []
    
    while len(possibles) > 0:
        a = random.randint(0, len(possibles)-1)
        new_pos.append(possibles[a])
        possibles.pop(a)

    for i in range(len(new_pos)):
        b = new_pos[i]
        new_slova.append(slova[b])
        new_definice.append(definice[b])

    slova = new_slova
    definice = new_definice

    if reverse:
        LoadDefinition()
    else:
        LoadWord()
    return


res_x = 900
res_y = 500
res = str(res_x)+"x"+str(res_y)
okno = tk.Tk()       
okno.title("Language cards")
okno.minsize(600, 400)  
okno.geometry(res)

score_wrong = tk.Label(okno, text=f"Wrong {not_know_count}", font=("Arial", 18))
score_wrong.place(relx=0.05, rely=0.05)

score_right = tk.Label(okno, text=f"Correct {know_count}", font=("Arial", 18))
score_right.place(relx=0.8, rely=0.05)

slovicko = tk.Label(okno, text=slova[0], font=("Arial", 28, "bold"))
slovicko.place(relx=0.5, rely=0.4, anchor="center")
if not reverse:
    LoadWord()
else:
    LoadDefinition()

show = tk.Label(okno, text="showing word", font=("Arial", 18))
show.place(relx=0.5, rely=0.1, anchor="center")

not_know_but = tk.Button(okno, text="Don't know", font=("Arial", 16), width=12, height=2, bg="#ff0d00", fg="black", command=NotKnow)
not_know_but.place(relx=0.25, rely=0.7, anchor="center")

know_but = tk.Button(okno, text="Know", font=("Arial", 16), width=12, height=2, bg="#00ff00", fg="black", command=Know)
know_but.place(relx=0.75, rely=0.7, anchor="center")

flip_but = tk.Button(okno, text="Flip", font=("Arial", 16), width=12, height=2, bg="#37b6ff", fg="black", command=Flip)
flip_but.place(relx=0.5, rely=0.7, anchor="center")

restart_but = tk.Button(okno, text="restart", font=("Arial", 10), width=6, height=1, bg="#000000", fg="white", command=Restart)
restart_but.place(relx=0.2, rely=0.9, anchor="center")

reverse_but = tk.Button(okno, text="reverse", font=("Arial", 10), width=6, height=1, bg="#000000", fg="white", command=Reverse)
reverse_but.place(relx=0.8, rely=0.9, anchor="center")

shuffle_but = tk.Button(okno, text="shuffle", font=("Arial", 10), width=6, height=1, bg="#000000", fg="white", command=Shuffle)
shuffle_but.place(relx=0.7, rely=0.9, anchor="center")

repeat_but = tk.Button(okno, text="Repeat", font=("Arial", 16), width=12, height=2, bg="#37b6ff", fg="black", command=Repeat)

okno.mainloop()
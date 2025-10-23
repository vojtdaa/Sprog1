

all_points = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x_points = []
o_points = []

desk = ["-"] * 9

win_combs = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

def Check():
    vysledek = 0
    for comb in win_combs:

        if all(point in x_points for point in comb):
            vysledek = 1
            return vysledek
        
        if all(point in o_points for point in comb):
            vysledek = 2
            return vysledek
    return vysledek

def Play():
    game_running = True
    vysledek = 0
    play = 0
    while game_running:
        play = input("Hrac 1 (x): Zadej cislo 1-9: ")
        if not play.isdigit(): 
            play = 0

        if int(play) in all_points:
            x_points.append(int(play))
            all_points.remove(int(play))
        else: print("Invalid move.")

        Display()

        if all_points == []:
            vysledek == 0
            return vysledek
        
        vysledek = Check()

        if vysledek == 1:
            return vysledek
        if vysledek == 2:
            return vysledek

        play = input("Hrac 2 (o): Zadej cislo 1-9: ")
        if not play.isdigit(): 
            play = 0
        if int(play) in all_points:
            o_points.append(int(play))
            all_points.remove(int(play))
        else: print("Invalid move.")

        Display()

        if all_points == []:
            vysledek == 0
            return vysledek
                
        vysledek = Check()

        if vysledek == 1:
            return vysledek
        if vysledek == 2:
            return vysledek
        
    return vysledek

        

def Display():
    for i in range(1, 10):
        if i in x_points:
            desk[i-1] = "x"
        if i in o_points:
            desk[i-1] = "o"
    print(desk[0], desk[1], desk[2])
    print(desk[3], desk[4], desk[5])
    print(desk[6], desk[7], desk[8])


print("hraci pole:")
print("1 2 3\n4 5 6\n7 8 9")
game_result = Play()

if game_result == 1:
    print("Player 1 (x) won!")
elif game_result == 2:
    print("Player 2 (o) won!")
else: print("It's a draw!")
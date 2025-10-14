import matplotlib.pyplot as plt
import random
import pandas as pd


# Načti soubor
df = pd.read_csv("people_heights_1000.csv")  

# Získej seznam bodů (x=vek, y=vyska)
points = list(zip(df["vek"], df["vyska"]))

# Pro kontrolu
print(points[:10])  # prvních 10 bodů

#points = [(1, 1), (2, 2), (2, 7), (-9, -7), (-7, 8), (6, -8)]

def GeneratePoints():
    for i in range(50):
        x = random.randint(-50, 50)
        noise = random.randint(-3, 3)
        y = 3*x + noise
        points.append((x, y))

x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

min_point = min(x_points)
max_point = max(x_points)

plt.scatter(x_points, y_points, color='red', s=20)


x_ratio = [n for n in range(round(min_point), round(max_point)+1, 1)]

# f: y = ax + b

a = 4
b = -0.5

start_a = a
start_b = b

step = 0.1
l_rate = 0.00001
pocet_iteraci = 10000

y_ratio = [a*n + b for n in x_ratio]

def Primka(a, b, color="black", label="výsledná přímka"):
    y_ratio = [a*n + b for n in x_ratio]
    plt.plot(x_ratio, y_ratio, color=color, label=label, linewidth=2)

def LossFunction(a, b):
    return sum((y - (x*a + b))**2 for x, y in points)/len(x_points)


def BestA(a, step=0.1):
    for _ in range(pocet_iteraci):
        loss_now = LossFunction(a, b)
        loss_after = LossFunction(a + step, b)
    
        if loss_now < loss_after:
            step = -step
        a += step
        step *= 0.99
    return a

def BestB(b, step=0.1):
    for _ in range(pocet_iteraci):
        loss_now = LossFunction(a, b)
        loss_after = LossFunction(a, b + step)
    
        if loss_now < loss_after:
            step = -step
        b += step
        step *= 0.99

    return b

def GetIdealValues(a, b, l_rate = 0.01):
    for i in range(pocet_iteraci):
       
        da = sum(-2*(x * (y - (a*x + b))) for x, y in points)/len(x_points)
        db = sum(-2* (y - (a*x + b)) for x, y in points)/len(x_points)

        a = a - l_rate * da
        b = b - l_rate * db

        if i % 1000 == 0:
            print(f"Iter {i:5d} | Loss: {LossFunction(a,b):.4f} | a={a:.3f} | b={b:.3f}")
    
    return a, b

a, b = GetIdealValues(a, b, l_rate)

print(f"a: {start_a}", f"-> {a}")
print(f"b: {start_b}", f"-> {b}")
print(f"loss function = {LossFunction(a, b)}")


Primka(a, b)
inputos = float(input("zadej x"))
print(f"k zadanemu {inputos} se nejvice blizi hodnota {inputos*a + b}")

plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.grid()
plt.show()
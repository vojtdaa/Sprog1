import matplotlib.pyplot as plt

points = [(1, 1), (2, 2), (2, 7), (-9, -7), (-7, 8), (6, -8)]

x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

min_point = min(x_points)
max_point = max(x_points)

for i in range(len(x_points)):
    plt.plot(x_points[i], y_points[i], marker=".", color='red', markersize=8)


x_ratio = [n for n in range(min_point, max_point+1, 1)]

# f: y = ax + b

a = 4
b = -0.5

start_a = a
start_b = b

step = 0.1
l_rate = 0.01
pocet_iteraci = 10000

y_ratio = [a*n + b for n in x_ratio]

def Primka():
    plt.plot(x_ratio, y_ratio, label = "", color = "#000000")

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
    for _ in range(pocet_iteraci):
       
        da = sum(-2*(x * (y - (a*x + b))) for x, y in points)/len(x_points)
        db = sum(-2* (y - (a*x + b)) for x, y in points)/len(x_points)

        a = a - l_rate * da
        b = b - l_rate * db
    
    return a, b

a, b = GetIdealValues(a, b, l_rate)

print(f"a: {start_a}", f"-> {a}")
print(f"b: {start_b}", f"-> {b}")
print(f"loss function = {LossFunction(a, b)}")

y_ratio = [a*n + b for n in x_ratio]
Primka()

plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.grid()
plt.show()
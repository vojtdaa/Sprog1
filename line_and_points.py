import matplotlib.pyplot as plt

points = [(5, 10), (2, -2), (-7, -3)]

x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

for i in range(len(x_points)):
    plt.plot(x_points[i], y_points[i], marker=".", color='red', markersize=8)


x_ratio = [n for n in range(-10, 11, 1)]

# f: y = ax + b

a = 1
b = -0.5

y_ratio = [a*n + b for n in x_ratio]

def Primka():
    plt.plot(x_ratio, y_ratio, label = "", color = "#000000")

def Difference_pa():
    dif = (y_points[0]-(a*x_points[0] + b))**2
    dif2 = (y_points[1]-(a*x_points[1] + b))**2
    return dif + dif2

values = []
val_min = Difference_pa()

for _ in range(100):
    dif = Difference_pa()
    if dif < val_min:
        val_min = dif
    values.append(dif)
    b+=1

print(val_min)

Primka()

plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.grid()
plt.show()
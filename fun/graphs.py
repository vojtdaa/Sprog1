import matplotlib.pyplot as plt
from math import sin, pi

# parametry
start = -2 * pi
end = 2 * pi
step = 0.1

# generace dat
x = []
y_sin = []
y_parabola = []

val = start
while val <= end:
    x.append(val)
    y_sin.append(sin(val))
    y_parabola.append(val**3/100)
    val += step

# vykreslení
plt.plot(x, y_sin, label="sin(x)", color="#00C850")
plt.plot(x, y_parabola, label=f"x^3", color="#6F00BE")
plt.axvline(0, color="black", linestyle="--", label="x=0")
plt.axhline(0, color="black", linestyle="--", label="y=0")
plt.title("sin(x) a škálovaná parabola")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
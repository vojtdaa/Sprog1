import matplotlib.pyplot as plt

# body
points = [[5,10], [2,-2], [-7,-3]]
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

# hyperparametry
m = 0.0       # počáteční sklon
b = 0.0       # počáteční průsečík
lr = 0.01     # learning rate
epochs = 200  # počet kroků

# nastavení grafu
plt.figure(figsize=(6,6))
for p in points:
    plt.plot(p[0], p[1], marker=".", color='red', markersize=12)

plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.xlim(-10, 10)
plt.ylim(-10, 15)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient descent: přímka se učí k bodům")

x_line = [-10, 10]

# animace
for epoch in range(epochs):
    # gradienty (směr, kam posunout m a b)
    dm = -2 * sum(x_vals[i] * (y_vals[i] - (m*x_vals[i] + b)) for i in range(len(points))) / len(points)
    db = -2 * sum((y_vals[i] - (m*x_vals[i] + b)) for i in range(len(points))) / len(points)
    
    # aktualizace parametrů současně
    m -= lr * dm
    b -= lr * db

    # vykreslení přímky pro aktuální krok
    y_line = [m*n + b for n in x_line]
    line, = plt.plot(x_line, y_line, color='blue', alpha=0.1)
    plt.pause(0.01)
    line.remove()

# finální přímka
y_line = [m*n + b for n in x_line]
plt.plot(x_line, y_line, color='blue', label=f'y = {m:.2f}x + {b:.2f}')
plt.legend()
plt.grid(True)
plt.show()

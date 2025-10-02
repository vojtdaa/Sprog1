import matplotlib.pyplot as plt

# Rozsah hrubých příjmů
before = [x for x in range(21000, 3000000, 5000)]

# Daňové sazby a hranice
low_rate = 0.15
high_rate = 0.23
threshold = 1_582_812  # 36 × průměrná mzda (43 967 Kč)

def progressive_tax(before, low_rate, high_rate, threshold):
    taxes = []
    for income in before:
        if income <= threshold:
            tax = income * low_rate
        else:
            tax = threshold * low_rate + (income - threshold) * high_rate
        taxes.append(tax)
    return taxes

after = progressive_tax(before, low_rate, high_rate, threshold)

# Graf
plt.plot(before, after, label="Daň", color="#FF0000")
plt.xlabel("Hrubý příjem (Kč)")
plt.ylabel("Výše daně (Kč)")
plt.title("Progresivní daň v ČR (2024)")
plt.axvline(threshold, color="blue", linestyle="--", label="Hranice 23 % sazby")
plt.legend()
plt.grid(True)
plt.show()
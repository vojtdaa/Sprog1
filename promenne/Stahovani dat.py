data_mass = float(input("data mass [MB] "))
download_speed = float(input("download speed [Mbit/s] "))
t = data_mass * 8 / download_speed
t = round(t, 2)
print(f"{t} s")
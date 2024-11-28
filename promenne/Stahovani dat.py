data_mass = int(input("data mass [MB] "))
download_speed = int(input("download speed [Mbit/s] "))
t = data_mass * 8 / download_speed
t = round(t, 2)
print(f"{t} s")
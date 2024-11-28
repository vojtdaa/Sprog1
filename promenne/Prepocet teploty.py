import math

temperature_celsius = int(input("temperature [°C]"))
temperature_kelvin = temperature_celsius * 273.15
temperature_farenheit = temperature_celsius * 9/5 + 32

temperature_farenheit = round(temperature_farenheit, 2)
temperature_kelvin = round(temperature_kelvin, 2)

print(f"{temperature_kelvin} K")
print(f"{temperature_farenheit} F")
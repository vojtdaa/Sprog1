import math

height = float(input("height "))
radius = float(input("radius "))
volume = math.pi * radius ** 2 * height
print(f"{volume} cm³")
surface = 2 * math.pi * radius * (radius + height)
print(f"{surface} cm²")
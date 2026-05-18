def vytvor_trojuhelnik(n):
    vysledek = ""
    for i in range(1, n+1):
        for _ in range(i):
            vysledek += "*"
        vysledek += "\n"
    return vysledek

print(vytvor_trojuhelnik(1))
# *

print(vytvor_trojuhelnik(3))
# *
# **
# ***

print(vytvor_trojuhelnik(5))
# *
# **
# ***
# ****
# *****
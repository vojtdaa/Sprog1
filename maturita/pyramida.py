def pyramida(n):
    spodni = 2*n-1
    vysledek = ""
    for i in range(1, spodni + 1, 2):

        for _ in range(int((spodni-i)/2)):
            vysledek += " "

        for _ in range(i):
            vysledek += "*"

        for _ in range(int((spodni-i)/2)):
            vysledek += " "
        
        vysledek += "\n"
    return vysledek


print(pyramida(3))
#   *
#  ***
# *****

print(pyramida(5))
#     *
#    ***
#   *****
#  *******
# *********
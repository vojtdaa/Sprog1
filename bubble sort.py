cisla = [5, 1, 4, 8, 2, 3]
change = True
step = 0

for i in range(len(cisla)):
    if change == False:
        break
    change = False
    for x in range(len(cisla)-1):
        step += 1
        if cisla[x] > cisla[x+1]:
            change  = True
            temp = cisla[x]
            cisla[x] = cisla[x+1]
            cisla[x+1] = temp

print(cisla)
print(step)
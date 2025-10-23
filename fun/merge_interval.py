seznam = [(1,3), (2,5), (10,12), (11,15)]

new = []
stop = False
complete = False
print(new)
while not stop:
    i = 0
    j = 0
    a = seznam[i][j]
    while a != seznam[i][j+1]:
        a = seznam[i][j]
        new.append(a)
        a += 1
        if a>10: break
    break

     

print(new)
seznam = [(1,3), (2,5), (10,12), (11,15)]

new = []
stop = False
complete = False

def MakeNew():
    for z in range(len(seznam)-1):
        Rozepis_interval(z, seznam, new)  
    return

def Rozepis_interval(start, seznam, new):
    a = seznam[start][0]
    while a <= seznam[start][1]:
        if a not in new:
            new.append(a)
            a += 1
    return new 
   
MakeNew()

print(new)
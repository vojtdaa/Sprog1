seznam = [(1,3), (2,5), (10,12), (11,15)]

new = []



def Rozepis_interval(start, seznam, new):
    a = seznam[start][0]
    while a <= seznam[start][1]:
        if a not in new:
            new.append(a)
        a += 1
    return new 

def MakeNew():
    for z in range(len(seznam)):
        Rozepis_interval(z, seznam, new)   
  
MakeNew()

def SliceIt(new):
    complete = []
    a = 0
    b = 0
    while a < len(new):
        while b <= len(new)-1 and new[b] == (new[a]+(b-a)):
            b += 1

        complete.append((new[a], new[b-1]))
        a = b
        
    return complete


print(new)
print(SliceIt(new))
seznam = [(5, 6), (1, 3), (2, 4), (8, 10), (9, 11), (15, 18), (17, 20)]
seznam = sorted(seznam)

def Merge(seznam):
    start = 0
    step = 0
    while start <= len(seznam)-2:
        min_val = seznam[start][0]
        max_val = seznam[start][1]

        new1 = seznam[start+1][0]
        new2 = seznam[start+1][1]
        if new1 >= min_val and new1 <= max_val:
            if new2 <= max_val:
                seznam[start] = (min_val, max_val)
                #seznam.pop(start+1)
            elif new2 > max_val:
                seznam[start] = (min_val, new2)
                #seznam.pop(start+1)
        elif new2 > min_val and new2 <= max_val:
            seznam[start] = (new1, max_val)
            #seznam.pop(start+1)
        elif new1 < min_val and new2 > max_val:
            seznam[start] = (new1, new2)
            #seznam.pop(start+1)   
        else: 
            start += 2 
        step += 1
    return seznam, step

print(Merge(seznam))
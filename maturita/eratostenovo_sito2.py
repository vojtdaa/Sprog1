def EratostenovoSito(pocet):
    seznam = [n+1 for n in range(pocet)]
    prvocisla = []
    index = 0

    for i in seznam:

        if i != 0 and i != 1:
            prvocisla.append(i)

            for a in range(index, len(seznam), i):
                seznam[a] = 0

        index += 1
        
    return prvocisla
        

print(EratostenovoSito(53))
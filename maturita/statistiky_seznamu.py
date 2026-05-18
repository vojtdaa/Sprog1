def max_lst(lst):
    nejvetsi = lst[0]
    for i in lst:
        if i > nejvetsi:
            nejvetsi = i

    return nejvetsi

def min_lst(lst):
    nejmensi = lst[0]
    for i in lst:
        if i < nejmensi:
            nejmensi = i

    return nejmensi

def prumer_lst(lst):
    soucet = 0
    pocet = 0

    for i in lst:
        pocet += 1
        soucet += i
    
    return soucet/pocet

def soucet_lst(lst):
    soucet = 0
    for i in lst:
        soucet += i

    return soucet

print(max_lst([3, 1, 4, 1, 5, 9]))    # → 9
print(min_lst([3, 1, 4, 1, 5, 9]))    # → 1
print(prumer_lst([1, 2, 3, 4, 5]))    # → 3.0
print(soucet_lst([1, 2, 3, 4, 5]))    # → 15
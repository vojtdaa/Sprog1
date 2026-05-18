def druhy_nejvetsi(lst):
    nejvetsi = lst[0]
    druhy = lst[0]

    for i in lst:
        if nejvetsi == druhy:
            if i < nejvetsi:
                druhy = i
        if i > nejvetsi:
            druhy = nejvetsi
            nejvetsi = i
        if i < nejvetsi and i > druhy:
            druhy = i
        
    return druhy


print(druhy_nejvetsi([3, 1, 4, 1, 5, 9, 2, 6]))   # → 6
print(druhy_nejvetsi([10, 5, 3, 8, 2]))            # → 8
print(druhy_nejvetsi([5, 5, 5]))                   # → 5
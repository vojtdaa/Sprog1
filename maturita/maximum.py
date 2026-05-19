def maximum(lst):
    nejvetsi = lst[0]

    def hledej(lst, nejvetsi):

        if not lst:
            return nejvetsi
        
        if lst[0] > nejvetsi:
            nejvetsi = lst[0]
        return hledej(lst[1:], nejvetsi)
    
    return hledej(lst, nejvetsi)

print(maximum([4, 2, 9, 1, 7]))    # → 9
print(maximum([10, 5, 3, 8, 2]))   # → 10
print(maximum([5]))                # → 5
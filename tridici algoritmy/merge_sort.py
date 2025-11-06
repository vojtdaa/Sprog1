
seznam = [5, 7, 8, 9, 6, 4, 1, 3, 10]
merge_steps = 0
def Merge(left, right):
    global merge_steps
    i = 0
    j = 0
    new = []
    while i < len(left) and j < len(right):
        merge_steps += 1
        if left[i] <= right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    while i < len(left):
        merge_steps += 1
        new.append(left[i])
        i += 1

    while j < len(right):
        merge_steps+= 1
        new.append(right[j])
        j += 1
    return new

def Merge_sort(seznam):
    if len(seznam) == 1:
        return seznam
    middle = len(seznam)//2
    left = Merge_sort(seznam[:middle])
    right = Merge_sort(seznam[middle:])

    
    return Merge(left, right)
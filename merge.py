seznam1 = [0, 7, 10]
seznam2 = [1, 3, 4, 8, 9, 10]

def Merge(left, right):
    i = 0
    j = 0
    new = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new.append(left[i])
            print(new)
            i += 1
        else:
            new.append(right[j])
            print(new)
            j += 1
    print(i, j)
    while i < len(left):
        new.append(left[i])
        i += 1

    while j < len(right):
        new.append(right[j])
        j += 1
    return new

print(Merge(seznam1, seznam2))
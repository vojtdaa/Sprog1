import random

seznam = [random.randint(1, 100) for _ in range(20)]

steps = 0

def QuickSort(n):
    global steps
    if len(n) <= 1:
        return n
    pivot = n[-1]
    j = -1

    for i in range(len(n)-1):
        steps+= 1
        if n[i] < pivot:
            steps+=1
            j += 1
            n[i], n[j] = n[j], n[i]
    
    left = n[0:j+1]
    right = n[j+1:-1]

    steps += 1

    return QuickSort(left) + [pivot] + QuickSort(right)


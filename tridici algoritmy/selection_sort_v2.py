import copy
import random
seznam = [1, 5, 4, 7, 8, 9, 6, 4, 3, 5, 1, 4]

def SelectionSort2(n):
    min = 0
    steps = 0
    for i in range(len(n)-1):
        min = i
        for x in range(i, len(n)):
            steps +=1
            if n[x] < n[min]:
                min = x

        n[i], n[min] = n[min], n[i]
    return steps


import copy

seznam = [22, 5, 61, 7, 3, 44, 8, 9]

def InsertionSort(n):
    steps = 0
    for i in range(1, len(n)):
        for z in range(i):
            steps += 1
            if n[i-z] < n[i-1-z]:
                n[i-z], n[i-1-z] = n[i-1-z], n[i-z]
                #print(n)
            else: break
    return steps

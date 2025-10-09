import copy

seznam = [22, 5, 61, 7, 3, 44, 8, 9]

def InsertionSort(n):
    steps = 0
    for i in range(1, len(n)):
        a = 0
        while a<i and n[i-a] < n[i-1-a]:
            steps += 1
            n[i-a], n[i-1-a] = n[i-1-a], n[i-a]
            a += 1
    return steps

print(InsertionSort(seznam))
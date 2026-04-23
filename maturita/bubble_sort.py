import random
import copy

seznam = [random.randint(1, 5*20) for _ in range(20)]

a = copy.deepcopy(seznam)
b = copy.deepcopy(seznam)
c = copy.deepcopy(seznam)


def Bubblesort(seznam):
    steps = 0
    for _ in range(len(seznam)):
        for i in range(len(seznam)-1):
            steps += 1
            if seznam[i] > seznam[i+1]:
                seznam[i], seznam[i+1] = seznam[i+1], seznam[i]
    return seznam, steps
print(Bubblesort(a))


def BetterBubbleSort(seznam):
    steps = 0
    for x in range(len(seznam)):
        changes = False
        for i in range(len(seznam)-1-x):
            steps += 1
            if seznam[i] > seznam[i+1]:
                seznam[i], seznam[i+1] = seznam[i+1], seznam[i]
                changes = True
        if changes == False:
            break
    return seznam, steps
    
print(BetterBubbleSort(b))

def BestBubbleSort(seznam):
    steps = 0
    left = 0
    right = len(seznam)-1

    for _ in range(len(seznam)//2):
        
        changes = False 
        for i in range(0, right):
            steps += 1
            if seznam[i] > seznam[i+1]:
                seznam[i], seznam[i+1] = seznam[i+1], seznam[i]
                changes = True
        left += 1

        if changes == False:
            break
        changes == False

        for i in range(right, left, -1):
            steps += 1
            if seznam[i-1] > seznam[i]:
                seznam[i-1], seznam[i] = seznam[i], seznam[i-1]
                changes = True

        right -= 1

        if changes == False:
            break

    return seznam, steps

print(BestBubbleSort(c))
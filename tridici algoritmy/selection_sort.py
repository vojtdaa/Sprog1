import random
import copy

rada = [5, 80, 0, 1, 24]
cisla = [4, 48, 5, 21, 20, 18, 16, 23, 22, 15, 24, 42, 2, 12, 25]


def SelectionSort(seznam):
    min = 0
    steps = 0
    for odkud in range(len(seznam)):
        min = odkud
        for y in range(odkud, len(seznam)):
            steps += 1
            if seznam[y] < seznam[min]:
                min = y

        seznam[odkud], seznam[min] = seznam[min], seznam[odkud]
    return steps


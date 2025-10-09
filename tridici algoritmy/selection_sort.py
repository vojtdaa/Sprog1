import random
import copy

rada = [5, 80, 0, 1, 24]
cisla = [4, 48, 5, 21, 20, 18, 16, 23, 22, 15, 24, 42, 2, 12, 25]


def SelectionSort(seznam):
    min_index = 0
    steps = 0
    for odkud in range(len(seznam)):
        min_index = odkud
        for y in range(odkud, len(seznam)):
            steps += 1
            if seznam[y] < seznam[min_index]:
                min_index = y

        seznam[odkud], seznam[min_index] = seznam[min_index], seznam[odkud]
    return steps


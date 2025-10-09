import random
import copy

from insertion_made_poorly import InsertionSort1
from insertion_sort import InsertionSort

insertion_1_res = []
insertion_2_res = []

def Compare():
    for value in range(10, 10000, 1000):
        nahodny_seznam = [random.randint(0, 5*value) for _ in range(value)]

        insertion_1_res.append(InsertionSort1(copy.deepcopy(nahodny_seznam)))
        insertion_2_res.append(InsertionSort(copy.deepcopy(nahodny_seznam)))
    
Compare()

print(insertion_1_res)
print(insertion_2_res)
    
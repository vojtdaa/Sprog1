import copy
import random
import time
#import matplotlib.pyplot as plt

from bubble_v1 import BubbleSort1
from bubble_v2 import BubbleSort2
from bubble_v3 import BubbleSort3
from bubble_v4 import BubbleSort4
from insertion_sort import InsertionSort

lists_lens = [n for n in range(10, 50, 10)]

def measure_sorts():
    print("measuring performance...")
    for kolikrat in range(50, 250, 50):
        unsorted_list = [random.randint(0, 5*kolikrat) for _ in range(kolikrat)]

        list_copy = copy.deepcopy(unsorted_list)

        time_start = time.perf_counter()
        comparisons = BubbleSort1(list_copy)
        time_end = time.perf_counter()

        execution_time = time_end - time_start

        print(f"Bubble v1 - pocet porovnani: {comparisons}, cas: {execution_time}")

        list_copy = copy.deepcopy(unsorted_list)

        time_start = time.perf_counter()
        comparisons = BubbleSort2(list_copy)
        time_end = time.perf_counter()

        execution_time = time_end - time_start


        print(f"Bubble v2 - pocet porovnani: {comparisons}, cas: {execution_time}")

        list_copy = copy.deepcopy(unsorted_list)

        time_start = time.perf_counter()
        comparisons = BubbleSort3(list_copy)
        time_end = time.perf_counter()

        execution_time = time_end - time_start


        print(f"Bubble v3 - pocet porovnani: {comparisons}, cas: {execution_time}")

        list_copy = copy.deepcopy(unsorted_list)

        time_start = time.perf_counter()
        comparisons = BubbleSort4(list_copy)
        time_end = time.perf_counter()

        execution_time = time_end - time_start

        print(f"Bubble v4 - pocet porovnani: {comparisons}, cas: {execution_time}")
        print("---------------------------------------")



#measure_sorts()
Bubble1_results = []
Bubble2_results = []
Bubble3_results = []
Bubble4_results = []
Insertion_results = []

def MakeChart():
    for value in range(10, 50, 10):
        nahodny_seznam = [random.randint(0, 5*value) for _ in range(value)]

        Bubble1_results.append(BubbleSort1(copy.deepcopy(nahodny_seznam)))
        Bubble2_results.append(BubbleSort2(copy.deepcopy(nahodny_seznam)))
        Bubble3_results.append(BubbleSort3(copy.deepcopy(nahodny_seznam)))
        Bubble4_results.append(BubbleSort4(copy.deepcopy(nahodny_seznam)))

    
MakeChart()

def Vysledek():
    print("velikost |  50  |  100  |  150  |  200  |")
    print(f"bubble v1| {Bubble1_results}")
    print(f"bubble v2| {Bubble2_results}")
    print(f"bubble v3| {Bubble3_results}")
    print(f"bubble v4| {Bubble4_results}")


def GenerateChart():

    plt.plot(lists_lens, Bubble1_results, label="bubbleV1", color="blue")
    plt.plot(lists_lens, Bubble2_results, label="bubbleV2", color="blue")
    plt.plot(lists_lens, Bubble3_results, label="bubbleV3", color="blue")
    plt.plot(lists_lens, Bubble4_results, label="bubbleV4", color="blue")

Vysledek()





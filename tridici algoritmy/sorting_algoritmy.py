import copy
import random
import matplotlib.pyplot as plt

from bubble_v1 import BubbleSort1
from bubble_v2 import BubbleSort2
from bubble_v3 import BubbleSort3
from bubble_v4 import BubbleSort4
from selection_sort import SelectionSort
from insertion_sort import InsertionSort
from shell_sort import ShellSort
from quick_sort_home import Quick_sort_counter, Partition

lists_lens = [n for n in range(1, 20, 2)] #idealni porovnani je pri 10, 100, 10



Bubble1_results = []
Bubble2_results = []
Bubble3_results = []
Bubble4_results = []
Insertion_results = []
Selection_results = []
ShellSort_results = []
QuickSort_results = []

def MakeChart():
    for value in range(1, 20, 2):
        nahodny_seznam = [random.randint(0, 5*value) for _ in range(value)]

        Bubble1_results.append(BubbleSort1(copy.deepcopy(nahodny_seznam)))
        Bubble2_results.append(BubbleSort2(copy.deepcopy(nahodny_seznam)))
        Bubble3_results.append(BubbleSort3(copy.deepcopy(nahodny_seznam)))
        Bubble4_results.append(BubbleSort4(copy.deepcopy(nahodny_seznam)))
        Insertion_results.append(InsertionSort(copy.deepcopy(nahodny_seznam)))
        Selection_results.append(SelectionSort(copy.deepcopy(nahodny_seznam)))
        ShellSort_results.append(ShellSort(copy.deepcopy(nahodny_seznam)))
        QuickSort_results.append(Quick_sort_counter(copy.deepcopy(nahodny_seznam)))

    
MakeChart()

def Vysledek():
    print("velikost | 50 | 100 | 150 | 200 |")
    print(f"bubble v1| {Bubble1_results}")
    print(f"bubble v2| {Bubble2_results}")
    print(f"bubble v3| {Bubble3_results}")
    print(f"bubble v4| {Bubble4_results}")
    print(f"insertion| {Insertion_results}")
    print(f"selection| {Selection_results}")
    print(f"shell sort| {ShellSort_results}")
    print(f"quick sort| {QuickSort_results}")


def GenerateChart():

    plt.plot(lists_lens, Bubble1_results, label="bubbleV1", color="#FF0000")
    plt.plot(lists_lens, Bubble2_results, label="bubbleV2", color="#FF9900")
    plt.plot(lists_lens, Bubble3_results, label="bubbleV3", color="#469412")
    plt.plot(lists_lens, Bubble4_results, label="bubbleV4", color="#1200AF")
    plt.plot(lists_lens, Insertion_results, label="insertion", color="#A32098")
    plt.plot(lists_lens, Selection_results, label="selection", color="#00CFF3")
    plt.plot(lists_lens, ShellSort_results, label="shell", color="#000000")
    plt.plot(lists_lens, QuickSort_results, label="quick", color="#FFD900")

    plt.legend()
    plt.show()

GenerateChart()




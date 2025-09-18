import copy
import random
import time

cisla = [5, 1, 4, 8, 2, 3]

print("measuring performance...")

def BubbleSort1(n):
    step = 0

    for i in range(len(n)):

        for x in range(len(n) - 1):
            step += 1

            if n[x] > n[x+1]:
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
    return step

def BubbleSort2(n):
    step = 0
    change = True

    for i in range(len(n)):
        if change == False:
            return step

        change = False

        for x in range(len(n) - 1):
            step += 1

            if n[x] > n[x+1]:
                change  = True
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
    return step

def BubbleSort3(n):
    step = 0
    change = True
    end = len(n) - 1

    for i in range(len(n)):
        if change == False:
            return step

        change = False

        for x in range(end):

            if x == end-1:
                if n[x] <= n[x+1]:
                    end -= 1
                    break
            
            step += 1
            if n[x] > n[x+1]:
                change  = True
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
    return step

rada = [5, 1, 2, 3, 9, 6, 4, ]

def BubbleSort4(n):
    change = True
    end = len(n) -1
    start = 0
    step = 1

    while change and start < end:
        for i in range(start, end):
            step +=1
            if(n[i] > n[i+1]):
                n[i], n[i+1] = n[i+1], n[i]
                change = True
        if not change:
            break
        end -= 1

        for i in range(end, start, -1):
            if(n[i] < n[i-1]):
                n[i], n[i-1] = n[i-1], n[i]
        start += 1
    
    return step




def measure_sorts():
    
    unsorted_list = [random.randint(0, 10000) for _ in range(1000)]

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



measure_sorts()
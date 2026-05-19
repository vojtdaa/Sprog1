def bubble_sort(lst):

    for x in range(len(lst)-1, -1, -1):
        for i in range(x):
            if lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]

    return lst

print(bubble_sort([64, 34, 25, 12, 22]))   # → [12, 22, 25, 34, 64]
print(bubble_sort([5, 1, 4, 2, 8]))        # → [1, 2, 4, 5, 8]
print(bubble_sort([1]))                    # → [1]
print(bubble_sort([3, 3, 2]))              # → [2, 3, 3]
        

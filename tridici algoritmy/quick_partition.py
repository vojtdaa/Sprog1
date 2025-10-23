

def partition(left, right, pivot, numbers):
    
    while left <= right:

        while numbers[left]<pivot:
            left += 1
        while pivot < numbers[right]:
            right -= 1

        if left <= right:
            temp = numbers[left]
            numbers[left] = numbers[right]
            numbers[right] = temp
            left += 1
            right -= 1

    return left

def QuickSort(left, right, numbers):
    if left < right:
        pivot = numbers[(left + right) // 2]
        mid = partition(left, right, pivot, numbers)
        QuickSort(left, mid - 1, numbers)
        QuickSort(mid, right, numbers)

numbers = [1, 5, 7, 8, 9, 6, 3, 4, 8]
left = 0
right = len(numbers)-1

print(numbers)
QuickSort(left, right, numbers)
print(numbers)


numbers = [9, 7, 5, 24, 14, 3, 25, 5, 6, 9, 8, 7, 4, 5, 7, 6, 9]


def Partition(left, right, pivot, nums, steps):
    steps = 0
    if len(nums) <= 1:
        steps += 1
        return nums
    if len(nums) == 2:
        steps += 1
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums

    while right > left:
        while nums[left] < pivot and left < right:
            left += 1
            
        while nums[right] > pivot and right > left:
            right -= 1

        if right >= left:
            steps += 1
            nums[right], nums[left] = nums[left], nums[right]
            right -=1
            left +=1

    left_side = nums[:left]
    right_side = nums[left:]

    if len(left_side) > 0:
        new_pivot_l = left_side[len(left_side)//2]
    else: new_pivot_l = 0

    if len(right_side) > 0:
        new_pivot_r = right_side[len(right_side)//2]
    else: new_pivot_r = 0
    global kroky
    kroky += steps


    return Partition(0, len(left_side)-1, new_pivot_l, left_side, steps) + Partition(0, len(right_side)-1, new_pivot_r, right_side, steps)


def Quick_sort_counter(numbers):
    global kroky
    kroky = 0
    left = 0
    right = len(numbers)-1
    pivot = numbers[len(numbers)//2]
    Partition(left, right, pivot, numbers, kroky)
    return kroky

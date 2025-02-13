e = [2, 3, 1, 3, 5, 6, 4]

max_number = 0
min_number = e[0]
sum_number = 0
count = 0

for i in e:
    if i > max_number:
        max_number = i

    if i < min_number:
        min_number = i

    count += 1
    sum_number += i
    
average = sum_number/count
print(max_number, min_number, int(average))
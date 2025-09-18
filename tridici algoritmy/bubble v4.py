import random

seznam = [random.randint(1, 50) for _ in range(20)]

def BubbleSort4(n):
    change = True
    end = len(n) -1
    start = 0
    steps = 1

    while change and start < end:
        for i in range(start, end):
            steps +=1
            if(n[i] > n[i+1]):
                n[i], n[i+1] = n[i+1], n[i]
                change = True
        if not change:
            break
        end -= 1
        print(n)

        for i in range(end, start, -1):
            if(n[i] < n[i-1]):
                n[i], n[i-1] = n[i-1], n[i]
        start += 1
        print(n)
    
    return steps, n

print(BubbleSort4(seznam))
        
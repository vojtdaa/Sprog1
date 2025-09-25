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

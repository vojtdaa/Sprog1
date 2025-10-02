def BubbleSort1(n):
    steps = 0

    for i in range(len(n)):

        for x in range(len(n) - 1):
            steps += 1

            if n[x] > n[x+1]:
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
    return steps

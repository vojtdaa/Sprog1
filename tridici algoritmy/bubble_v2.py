def BubbleSort2(n):
    steps = 0
    change = True

    for i in range(len(n)):
        if change == False:
            return steps

        change = False

        for x in range(len(n) - 1):
            steps += 1

            if n[x] > n[x+1]:
                change  = True
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
    return steps
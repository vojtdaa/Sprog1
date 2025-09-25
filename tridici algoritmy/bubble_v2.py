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
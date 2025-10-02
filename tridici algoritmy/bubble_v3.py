def BubbleSort3(n):
    steps = 0
    change = True
    end = len(n) - 1

    for i in range(len(n)):
        if change == False:
            return steps

        change = False

        for x in range(end):

            if x == end-1:
                if n[x] <= n[x+1]:
                    end -= 1
                    break
            
            steps += 1
            if n[x] > n[x+1]:
                change  = True
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
    return steps
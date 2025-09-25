def BubbleSort3(n):
    step = 0
    change = True
    end = len(n) - 1

    for i in range(len(n)):
        if change == False:
            return step

        change = False

        for x in range(end):

            if x == end-1:
                if n[x] <= n[x+1]:
                    end -= 1
                    break
            
            step += 1
            if n[x] > n[x+1]:
                change  = True
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
    return step
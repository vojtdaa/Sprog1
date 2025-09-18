rada = [5, 1, 2, 3, 6, 4]


def BubbleSort3(n):
    step = 0
    change = True
    end = len(n) - 1

    for i in range(len(n)):

        change = False

        for x in range(end):
            print(n)
            if x == end:
                if n[x] <= n[x+1]:
                    end -= 1
                    break
            
            step += 1
            if n[x] > n[x+1]:
                change  = True
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
        if change == False:
            break
    return step

BubbleSort3(rada)
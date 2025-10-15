seznam = [2, 5, 6, 8, 7, 4, 3, 6, 2, 1, 7]

def ShellSort(n):
    steps = 0
    gap = len(n)//2
    while gap >= 1:
        for od in range(gap):
            for i in range(gap+od, len(n), gap):
                a = 0
                steps += 1
                while i - gap*(a+1) >= 0 and n[i-a*gap] < n[i-(a+1)*gap]:
                    n[i-a*gap], n[i-(a+1)*gap] = n[i-(a+1)*gap], n[i-a*gap]
                    a+=1   
        gap //= 2
    return steps

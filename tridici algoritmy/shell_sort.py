seznam = [2, 5, 6, 8, 7, 4, 3, 6, 2]

def ShellSort(n):
    steps = 0
    for gap in range(len(n)//2, 0, -1):
        for od in range(gap):
            for i in range(gap+od, len(n), gap):
                for z in range(0, i, gap):
                    steps += 1
                    if n[i-z] < n[i-gap-z]:
                        n[i-z], n[i-gap-z] = n[i-gap-z], n[i-z]
                        
                    else: break
    return steps
print(ShellSort(seznam))

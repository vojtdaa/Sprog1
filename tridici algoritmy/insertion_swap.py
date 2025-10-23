seznam = [4, 3, 2, 1]

def FindSmaller(n):
    last_index = len(n)-1
    gap = 1
    i = 0

    while last_index - (i+1) * gap >= 0 and n[last_index-i*gap] < n[last_index-(i+1)*gap]:
        n[last_index-i*gap], n[last_index-(i+1)*gap] = n[last_index-(i+1)*gap], n[last_index-i*gap]
        i+=1

    return n




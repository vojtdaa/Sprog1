seznam = [n+1 for n in range(30)]
plan = [1 for _ in range(30)]

print(seznam)
print(plan)

for i in range(1, len(seznam)):
    if plan[i] == 1:
        for x in range((i+1)**2, len(seznam)+1, i+1):
            plan[x-1] = 0

for a in range(1, len(plan)):
    if plan[a] == 1:
        print(seznam[a])
    
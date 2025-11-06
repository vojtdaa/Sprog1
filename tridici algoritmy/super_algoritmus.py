import time
import random
import copy

from merge_sort import Merge_sort

pocet_cisel = 10000
nahodny_seznam = [random.randint(0, 10000) for _ in range(pocet_cisel)]

start_time = time.time()
vysledek = sorted(copy.deepcopy(nahodny_seznam))
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Uplynulý čas: {elapsed_time} sekund")

start_time = time.time()

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Uplynulý čas: {elapsed_time} sekund")
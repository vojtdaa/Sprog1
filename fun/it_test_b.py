'''
zakazana_cisla = [5, 6, 10, 24]

for i in range(1, 101):
    if i not in zakazana_cisla:
        print(i)'''

#faktorial 5! = 5*4*3*2*1
faktorial = int(input("Vloz cislo: "))
print(f"{faktorial}", end=" * ")

for i in range(faktorial-1, 0, -1):
    faktorial *= i
    print(f"{i}", end=" * ")

if faktorial == 0:
    faktorial = 1
print(f"\n {faktorial}")
n = int(input("Zadej vysku trojuhelniku: "))

spodni = 2*n - 1
#mezera1 = n-i

def Cely(n):
    for i in range(1, n+1):
        for x in range(n-i):
            print("O", end="")

        for x in range(i+(i-1)):
            print("X", end="")

        for x in range(n-i):
            print("O", end="")
        print("\n")

def Obvod(n):
    for i in range(1, n+1):
        
        if i == n:
            for _ in range(2*n-1):
                print("X", end="")
            break
        else:
            for x in range(n-i):
                print("O", end="")

            print("X", end="")
            if i != 1:
                for _ in range(2*n-3):
                    print("O", end="")
                print("X", end="")
            
        
            

            for x in range(n-i):
                print("O", end="")
            print("\n")     

Obvod(n)

2*n - 3
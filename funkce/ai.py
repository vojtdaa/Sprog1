a = [1, 2]
b = [3, 6]
c = [4, 8]
d = [5, 10]

body_y = {1: 2, 2: 6, 3: 8, 4: 10}
body_x = {1: 1, 2: 3, 3: 4, 4: 5}


# f: y = kx

def Cost_function(k):
    cost_function = 0
    for i in range(1, 4+1):
        cost_function += (body_y[i] - body_x[i]*k)**2
    
    if cost_function != 0:
        return 1/cost_function
    else: return 0




print(Cost_function(2))
print(Cost_function(1))
print(Cost_function(0))
print(Cost_function(-2))
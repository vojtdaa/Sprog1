import tkinter as tk
import math

root = tk.Tk()
root.title("Cube")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# spojit 0, 1 | 1, 2 | 2, 3 | 3, 0
# Vytvoření čáry
points = [[1, 0, 0], [0, 0, 0], [0, 1, 0], [1, 1, 0],
          [1, 0, 1], [0, 0, 1], [0, 1, 1], [1, 1, 1]]

s = [0, 0, 0]

lines = []
scale = 150
radius = 1
alfa = 1
beta = 1
gamma = 0
iteration = 0

def DrawPoints():
    global scale
    global s
    global points
    global radius
    posun = 200
    pi_4 = math.pi/4
    #definice bodů s rotaci podle osy z meni se x, y
    for i in range(4):
        points[i][0] = s[0] + math.cos(alfa + (1+2*i) * (math.pi / 4))
        points[i][1] = s[1] - math.sin(alfa + (1+2*i) * (math.pi / 4))
    for i in range(4):
        points[i+4][0] = s[0] + math.cos(alfa + (1+2*i) * (math.pi / 4))
        points[i+4][1] = s[1] - math.sin(alfa + (1+2*i) * (math.pi / 4))

    #rotace podle osy x - meni se pouze y
    for i in range(4):
        angle = alfa + (1 + 2*i) * pi_4
        atan_val = math.atan2(math.sqrt(2) * math.sin(angle), 1)

        sin_beta = math.sin(beta)
        cos_beta = math.cos(beta)
        sin_atan = math.sin(atan_val)
        cos_atan = math.cos(atan_val)

        points[i][1] = s[1] - (sin_beta * cos_atan + cos_beta * sin_atan)
        points[i+4][1] = points[i][1] 
    '''points[0][1] = s[1] - (math.sin(beta)*math.cos(math.atan2((math.sqrt(2)*math.sin(pi_4+alfa)), 1)) + math.cos(beta) * math.sin(math.atan2((math.sqrt(2)*math.sin(pi_4+alfa)), 1)))
    points[1][1] = s[1] - (math.sin(beta)*math.cos(math.atan2((math.sqrt(2)*math.sin(3*pi_4+alfa)), 1)) + math.cos(beta) * math.sin(math.atan2((math.sqrt(2)*math.sin(3*pi_4+alfa)), 1)))
    points[2][1] = s[1] - (math.sin(beta)*math.cos(math.atan2((math.sqrt(2)*math.sin(5*pi_4+alfa)), 1)) + math.cos(beta) * math.sin(math.atan2((math.sqrt(2)*math.sin(5*pi_4+alfa)), 1)))
    points[3][1] = s[1] - (math.sin(beta)*math.cos(math.atan2((math.sqrt(2)*math.sin(7*pi_4+alfa)), 1)) + math.cos(beta) * math.sin(math.atan2((math.sqrt(2)*math.sin(7*pi_4+alfa)), 1)))'''
    
    #vykreslení bodů
    for i in range(4):
        n = (i+5)%4
        x1, y1 = points[i][0], points[i][1]
        x2, y2 = points[n][0], points[n][1]

        canvas.create_line(x1*scale+posun, y1*scale+posun, x2*scale+posun, y2*scale+posun, dash=5)
    for i in range(4):
        n = (i+5)%4+4
        x1, y1 = points[i+4][0], points[i+4][1]
        x2, y2 = points[n][0], points[n][1]

        canvas.create_line(x1*scale+posun, y1*scale+posun, x2*scale+posun, y2*scale+posun)


DrawPoints()
root.mainloop()
import tkinter as tk
import math

root = tk.Tk()
root.title("Cube")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# spojit 0, 1 | 1, 2 | 2, 3 | 3, 0
# Vytvoření čáry
points_x = [1, 0, 0, 1]
points_y = [0, 0, 1, 1]
points_xz = [1, 0, 0, 1]
points_yz = [0, 0, 1, 1]
lines = []
scale = 150
radius = math.sqrt(2)/2
mid_point = [300, 200]
alfa = 0
beta = 0
gamma = 0
iteration = 0

def DrawSquare(posun = 150):
    global points_x
    global points_y
    global lines
    global scale
    canvas.delete(*lines)
    lines = []
    for i in range(0, -len(points_x), -1):
        line = canvas.create_line(points_x[i]*scale+posun, points_y[i]*scale+posun, points_x[i-1]*scale+posun, points_y[i-1]*scale+posun)
        lines.append(line)
    lines = []
    return

def DrawCube():
    global points_x
    global points_y
    global points_xz
    global points_yz
    global lines
    global scale
    global radius
    global alfa
    canvas.delete(*lines)
    lines = []

    #bod 1: x = s(x)/scale+cos(alfa+(1+2*i)*pi/4)*r/scale
    #bod 1: y = s(y)/scale+sin(alfa+(1+2*i)*pi/4)*r/scale

    for i in range(len(points_x)):
        points_x[i] = mid_point[0]/scale + math.cos(alfa + (1+2*i) * (math.pi / 4)) * radius
        points_y[i] = mid_point[1]/scale - math.sin(alfa + (1+2*i) * (math.pi / 4)) * radius
    print(points_x, points_y)

    for i in range(len(points_xz)):
        points_xz[i] = (mid_point[0]/scale + math.cos(alfa + (1+2*i) * (math.pi / 4)) * radius)#+0.5*math.cos(math.pi/4)
        points_yz[i] = (mid_point[1]/scale - math.sin(alfa + (1+2*i) * (math.pi / 4)) * radius)#-0.5*math.sin(math.pi/4) 

    print(points_xz, points_yz)
    for i in range(0, -len(points_xz), -1):
        line = canvas.create_line(points_xz[i]*scale, points_yz[i]*scale, points_xz[i-1]*scale, points_yz[i-1]*scale)
        lines.append(line)

    for i in range(4):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_xz[i]*scale, points_yz[i]*scale)
        lines.append(line)

    for i in range(0, -len(points_x), -1):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_x[i-1]*scale, points_y[i-1]*scale)
        lines.append(line)

    alfa = math.pi/60
    canvas.after(20, DrawCube)
    
canvas.create_rectangle(mid_point[0]-5, mid_point[1]-5, mid_point[0]+5, mid_point[1]+5, fill="red", outline="")
def CubeRotY():
    global iteration
    global points_x
    global points_y
    global points_xz
    global points_yz
    global lines
    global scale
    global radius
    global beta
    canvas.delete(*lines)
    lines = []

    #bod 1: x = s(x)/scale+cos(alfa+(1+2*i)*pi/4)*r
    #bod 1: y = s(y)/scale+sin(alfa+(1+2*i)*pi/4)*r
    points_x[0] = mid_point[0]/scale + math.cos(beta + 7 * math.pi / 4) * radius
    #points_y[0] = mid_point[1]/scale + 0.5

    points_x[1] = mid_point[0]/scale + math.cos(beta + 5 * math.pi / 4) * radius
    #points_y[1] = mid_point[1]/scale + 0.5

    points_x[2] = mid_point[0]/scale + math.cos(beta + 5 * math.pi / 4) * radius
    #points_y[2] = mid_point[1]/scale - 0.5

    points_x[3] = mid_point[0]/scale + math.cos(beta + 7 * math.pi / 4) * radius
    #points_y[3] = mid_point[1]/scale - 0.5

    points_xz[0] = mid_point[0]/scale + math.cos(beta + 1 * (math.pi / 4)) * radius
    #points_yz[0] = mid_point[1]/scale + 0.5

    points_xz[1] = mid_point[0]/scale + math.cos(beta + 3 * (math.pi / 4)) * radius
    #points_yz[1] = mid_point[1]/scale + 0.5

    points_xz[2] = mid_point[0]/scale + math.cos(beta + 3 * (math.pi / 4)) * radius
    #points_yz[2] = mid_point[1]/scale - 0.5

    points_xz[3] = mid_point[0]/scale + math.cos(beta + 1 * (math.pi / 4)) * radius
    #points_yz[3] = mid_point[1]/scale - 0.5
    print(points_xz, points_yz)

    for i in range(0, -len(points_xz), -1):
        line = canvas.create_line(points_xz[i]*scale, points_yz[i]*scale, points_xz[i-1]*scale, points_yz[i-1]*scale)
        lines.append(line)

    for i in range(4):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_xz[i]*scale, points_yz[i]*scale)
        lines.append(line)

    for i in range(0, -len(points_x), -1):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_x[i-1]*scale, points_y[i-1]*scale)
        lines.append(line)

    beta += math.pi/60
    #alfa += math.pi/60

    iteration+=1
    canvas.after(100, CubeRotX)
    '''if iteration == 100:
        iteration = 0
        canvas.after(20, CubeRotZ)
    else:
        canvas.after(20, CubeRotY)'''

def CubeRotZ():
    global iteration
    global points_x
    global points_y
    global points_xz
    global points_yz
    global lines
    global scale
    global radius
    global alfa
    canvas.delete(*lines)
    lines = []

    #bod 1: x = s(x)/scale+cos(alfa+(1+2*i)*pi/4)*r
    #bod 1: y = s(y)/scale+sin(alfa+(1+2*i)*pi/4)*r
    points_x[0] = mid_point[0]/scale + math.cos(alfa + 1 * math.pi / 4) * radius
    points_y[0] = mid_point[1]/scale - math.sin(alfa + 1 * math.pi / 4) * radius

    points_x[1] = mid_point[0]/scale + math.cos(alfa + 3 * math.pi / 4) * radius
    points_y[1] = mid_point[1]/scale - math.sin(alfa + 3 * math.pi / 4) * radius

    points_x[2] = mid_point[0]/scale + math.cos(alfa + 5 * math.pi / 4) * radius
    points_y[2] = mid_point[1]/scale - math.sin(alfa + 5 * math.pi / 4) * radius

    points_x[3] = mid_point[0]/scale + math.cos(alfa + 7 * math.pi / 4) * radius
    points_y[3] = mid_point[1]/scale - math.sin(alfa + 7 * math.pi / 4) * radius

    points_xz[0] = mid_point[0]/scale + math.cos(alfa + 1 * math.pi / 4) * radius
    points_yz[0] = mid_point[1]/scale - math.sin(alfa + 1 * math.pi / 4) * radius

    points_xz[1] = mid_point[0]/scale + math.cos(alfa + 3 * math.pi / 4) * radius
    points_yz[1] = mid_point[1]/scale - math.sin(alfa + 3 * math.pi / 4) * radius

    points_xz[2] = mid_point[0]/scale + math.cos(alfa + 5 * math.pi / 4) * radius
    points_yz[2] = mid_point[1]/scale - math.sin(alfa + 5 * math.pi / 4) * radius

    points_xz[3] = mid_point[0]/scale + math.cos(alfa + 7 * math.pi / 4) * radius
    points_yz[3] = mid_point[1]/scale - math.sin(alfa + 7 * math.pi / 4) * radius
    print(points_xz, points_yz)

    for i in range(0, -len(points_xz), -1):
        line = canvas.create_line(points_xz[i]*scale, points_yz[i]*scale, points_xz[i-1]*scale, points_yz[i-1]*scale)
        lines.append(line)

    for i in range(4):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_xz[i]*scale, points_yz[i]*scale)
        lines.append(line)

    for i in range(0, -len(points_x), -1):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_x[i-1]*scale, points_y[i-1]*scale)
        lines.append(line)

    alfa += math.pi/60
    canvas.create_rectangle(mid_point[0]-5, mid_point[1]-5, mid_point[0]+5, mid_point[1]+5, fill="red", outline="")

    iteration+=1
    if iteration == 100:
        iteration = 0
        canvas.after(20, CubeRotX)
    else:
        canvas.after(20, CubeRotZ)
    
    

def CubeRotX():
    global iteration
    global points_x
    global points_y
    global points_xz
    global points_yz
    global lines
    global scale
    global radius
    global alfa
    canvas.delete(*lines)
    lines = []

    #bod 1: x = s(x)/scale+cos(alfa+(1+2*i)*pi/4)*r
    #bod 1: y = s(y)/scale+sin(alfa+(1+2*i)*pi/4)*r
    #points_x[0] = mid_point[0]/scale + 0.5
    points_y[0] = mid_point[1]/scale - math.sin(alfa + 1 * math.pi / 4) * radius

    #points_x[1] = mid_point[0]/scale - 0.5
    points_y[1] = mid_point[1]/scale - math.sin(alfa + 1 * math.pi / 4) * radius

    #points_x[2] = mid_point[0]/scale - 0.5
    points_y[2] = mid_point[1]/scale - math.sin(alfa + 7 * math.pi / 4) * radius

    #points_x[3] = mid_point[0]/scale + 0.5
    points_y[3] = mid_point[1]/scale - math.sin(alfa + 7 * math.pi / 4) * radius

    #points_xz[0] = mid_point[0]/scale + 0.5
    points_yz[0] = mid_point[1]/scale - math.sin(alfa + 3 * math.pi / 4) * radius

    #points_xz[1] = mid_point[0]/scale - 0.5
    points_yz[1] = mid_point[1]/scale - math.sin(alfa + 3 * math.pi / 4) * radius

    #points_xz[2] = mid_point[0]/scale - 0.5
    points_yz[2] = mid_point[1]/scale - math.sin(alfa + 5 * math.pi / 4) * radius

    #points_xz[3] = mid_point[0]/scale + 0.5
    points_yz[3] = mid_point[1]/scale - math.sin(alfa + 5 * math.pi / 4) * radius
    print(points_xz, points_yz)

    for i in range(0, -len(points_xz), -1):
        line = canvas.create_line(points_xz[i]*scale, points_yz[i]*scale, points_xz[i-1]*scale, points_yz[i-1]*scale)
        lines.append(line)

    for i in range(4):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_xz[i]*scale, points_yz[i]*scale)
        lines.append(line)

    for i in range(0, -len(points_x), -1):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_x[i-1]*scale, points_y[i-1]*scale)
        lines.append(line)

    alfa += math.pi/60
    canvas.create_rectangle(mid_point[0]-5, mid_point[1]-5, mid_point[0]+5, mid_point[1]+5, fill="red", outline="")

    iteration+=1
    canvas.after(100, CubeRotY)
    '''if iteration == 100:
        iteration = 0
        canvas.after(20, CubeRotY)
    else:
        canvas.after(20, CubeRotX)'''

    

def DrawByCircle():
    global points_x
    global points_y
    global lines
    global scale
    global radius
    global alfa
    canvas.delete(*lines)
    lines = []
    #bod 1: x = s(x)/scale+cos(alfa+i*pi/4)*r/scale
    #bod 1: y = s(y)/scale+sin(alfa+i*pi/4)*r/scale
    for i in range(len(points_x)):
        points_x[i] = mid_point[0]/scale + math.cos(alfa + (1+2*i) * (math.pi / 4)) * radius
        points_y[i] = mid_point[1]/scale - math.sin(alfa + (1+2*i) * (math.pi / 4)) * radius
    print(points_x, points_y)       

    for i in range(0, -len(points_x), -1):
        line = canvas.create_line(points_x[i]*scale, points_y[i]*scale, points_x[i-1]*scale, points_y[i-1]*scale)
        lines.append(line)
    alfa+=math.pi/60
    canvas.after(20, DrawByCircle)
    return

def Line():
    global points_x
    global points_y
    global scale
    off = 100
    canvas.create_line(points_x[0]*scale+off, points_y[0]*scale+off, points_x[1]*scale+off, points_y[1]*scale+off, 
                       points_x[2]*scale+off, points_y[2]*scale+off, points_x[3]*scale+off, 
                       points_y[3]*scale+off, points_x[0]*scale+off, points_y[0]*scale+off)   

done = 0
distance = 100
time = 1000

def Move():
    global points_x
    global points_y
    global lines
    global done
    global scale
    global time
    global distance

    ms = 20
    frames = time/ms

    last_step = distance-done
    
    step = distance/frames

    done += step
    
    
    if done > distance:
        step = last_step
        points_x = [x + step/scale for x in points_x]
        DrawSquare()
        return
    else:
        points_x = [x + step/scale for x in points_x]
        DrawSquare()
        canvas.after(ms, Move)

DrawByCircle()
CubeRotX()
root.mainloop()
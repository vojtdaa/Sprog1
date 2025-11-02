import tkinter as tk
import time

width = 600
height = 600
ball_radius = 20

root=tk.Tk()
root.title("Jumping ball")

canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()


x_pos = width//2
y_pos = height-ball_radius
g = 0.5
velocity_0 = 0.1
frames = 60
akcelerace = 0.1
ball = canvas.create_oval(x_pos-ball_radius, y_pos-ball_radius, x_pos+ball_radius, y_pos+ball_radius)

def Animation():
    global velocity_0
    global frames
    global g
    
    canvas.coords(ball, x_pos - ball_radius, y_pos - ball_radius + velocity_0*frames+1/2*(-g)*frames, x_pos + ball_radius, y_pos + ball_radius)
    canvas.after(round(1000/frames), Animation)

Animation()
root.mainloop()
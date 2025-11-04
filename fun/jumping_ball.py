import tkinter as tk

width = 600
height = 600
ball_radius = 20

root=tk.Tk()
root.title("Jumping ball")

canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

x_pos = width//2
y_pos = height-ball_radius
floor = y_pos

g = 0.5
velocity_0 = 0
power = -15
ball = canvas.create_oval(x_pos-ball_radius, y_pos-ball_radius, x_pos+ball_radius, y_pos+ball_radius)
velocity_0 = power
def Jump():
    global velocity_0
    global power
    global floor
    if y_pos == floor:
        velocity_0 = power
        Animation()
        return
    else: return

def Animation():
    global ball_radius
    global velocity_0
    global g
    global floor
    global y_pos
    global x_pos
    
    velocity_0 += g
    y_pos += velocity_0
    if y_pos > floor:
        y_pos = floor
        canvas.coords(ball, x_pos - ball_radius, y_pos - ball_radius, x_pos + ball_radius, y_pos + ball_radius)
        velocity_0 = 0
    else:
        canvas.after(20, Animation)
        canvas.coords(ball, x_pos - ball_radius, y_pos - ball_radius, x_pos + ball_radius, y_pos + ball_radius)
    return


jump_but = tk.Button(root, text="Jump", font=("Arial", 16), width=12, height=2, bg="#ff0d00", fg="black", command=Jump)
jump_but.place(relx=0.25, rely=0.7, anchor="center")

Animation()

root.mainloop()
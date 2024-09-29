from tkinter import *
import math

root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.pack()

c.create_oval(100, 100, 500, 500, outline="black", width=5)
ball = c.create_oval(180, 180, 140, 140, fill='skyblue')

x, y = 300, 300
r = 200
angle = 0
speed = 10
direction = 1 # 1 - по часовой, -1 - против часовой

def change_direction():
    global direction
    direction *= -1

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed = max(1, speed - 1)

buttonDirection = Button(root, text='Смена направления', command=change_direction)
buttonDirection.pack(side=LEFT, padx=10, pady=10)

buttonSpeed1 = Button(root, text='  +  ', command=increase_speed)
buttonSpeed1.pack(side=RIGHT, padx=10, pady=10)

buttonSpeed2 = Button(root, text='  -  ', command=decrease_speed)
buttonSpeed2.pack(side=RIGHT, padx=0, pady=10)

def motion():
    global angle

    newx = x + r * math.cos(math.radians(angle))
    newy = y + r * math.sin(math.radians(angle))

    c.coords(ball, newx - 30, newy - 30, newx + 30, newy + 30)
    angle += (speed * direction)
    root.after(20, motion)

motion()

root.mainloop()
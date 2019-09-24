import turtle
import math
ProfLiTheG = turtle.Turtle()
ProfLiTheG.pensize(5)
print (ProfLiTheG)
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t,length, n)
circle (ProfLiTheG, 100)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def move (t, x, y):
    t.pu()
    t.setpos(x,y)
    t.pd() 

move (ProfLiTheG, 10, 100)
arc (ProfLiTheG, 50, 180)
move (ProfLiTheG, 10,100)
arc (ProfLiTheG, 50, 180)
move (ProfLiTheG, 10, 30)
circle (ProfLiTheG, 15)
move (ProfLiTheG, 10, 130)
circle (ProfLiTheG, 15)

turtle.mainloop()
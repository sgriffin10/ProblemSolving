import turtle
import math
ProfLiTheG = turtle.Turtle()
ProfLiTheG.speed(0)

print(ProfLiTheG)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t,r):
    circumference = 2*math.pi*r
    n=100
    length=circumference/n
    polygon(t, n, length)

circle(ProfLiTheG, 100)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def move(t, x, y):
    t.pu()
    t.setpos(x,y)
    t.pd()

ProfLiTheG.left(60)
arc(ProfLiTheG,100,120)
ProfLiTheG.left (120)
arc (ProfLiTheG, 100, 120)
ProfLiTheG.left (120)
arc (ProfLiTheG, 100, 120)
move (ProfLiTheG,0,200)
ProfLiTheG.right(60)
arc (ProfLiTheG, 100, 120)
ProfLiTheG.left (120)
arc (ProfLiTheG, 100, 120)
ProfLiTheG.left (120)
arc (ProfLiTheG, 100, 120)    

turtle.mainloop()
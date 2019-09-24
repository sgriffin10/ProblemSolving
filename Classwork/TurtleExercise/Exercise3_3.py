import turtle
import math

ProfLiTheG = turtle.Turtle()
ProfLiTheG.speed(3)
print (ProfLiTheG)

def polyline(t, n , length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t,length, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def move (t, x, y):
    t.pu()
    t.setpos(x,y)
    t.pd() 

turtle.circle(100, 360)
turtle.position()
circle(ProfLiTheG, 100)
ProfLiTheG.left(90)
move (ProfLiTheG, 0, 100)
polygon (ProfLiTheG, 100, 3)
move (ProfLiTheG,50, 10)
ProfLiTheG.left (60)
polygon (ProfLiTheG, 100, 3)
move (ProfLiTheG, 0, 100)
ProfLiTheG.right(155)
polygon (ProfLiTheG, 100, 3)
move (ProfLiTheG, 0, 100)
ProfLiTheG.right(170)
polygon (ProfLiTheG, 100, 3)
move (ProfLiTheG, 12, 60)
circle (ProfLiTheG, 27)
move (ProfLiTheG, 12, 180)
circle (ProfLiTheG, 27)
move (ProfLiTheG, 70, 118)
circle (ProfLiTheG, 27)
move (ProfLiTheG, -48, 118)
circle (ProfLiTheG, 27)
turtle.mainloop()
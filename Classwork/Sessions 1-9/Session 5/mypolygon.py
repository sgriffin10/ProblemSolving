import turtle
import math

ProfLiTheGod = turtle.Turtle()
ProfLiTheGod.speed(0)
print(ProfLiTheGod)
turtle.mainloop

#refactored code 
 
def polyline(t, n , length, angle):
    """ frees up the code"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# Exercise 2.1
# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
# square(ProfLiTheGod)

# Exercise 2.2
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
# square(ProfLiTheGod, 100)

# Exercise 2.3
# def polygon(t, n, length):        
#      angle = 360/n
#      polyline(t, n, length, angle)



# polygon(ProfLiTheGod, 5, 100)

# Exercise 2.4
# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = 100 
#     length = circumference/n
#     polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n=int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

# arc(ProfLiTheGod, 45, 360)

def circle(t, r):
    arc(t, r, 360)

circle(ProfLiTheGod, 100)

# circle(ProfLiTheGod, 50)

# REFACTORING











# pentagon(jack)
# circle (jack, 5)


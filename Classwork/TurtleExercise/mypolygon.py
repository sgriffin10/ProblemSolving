import turtle
import math

jack = turtle.Turtle()
print(jack)
turtle.mainloop

# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)

# def pentagon(t):
#     for i in range(5):
#         t.fd(100)
#         t.lt(72)

def circle(t,r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

# square(jack)
# pentagon(jack)
circle (jack, 5)


import turtle
from myFunctionfile import *
bob = turtle.Turtle()
turtle.colormode(255)                           
bob.speed(0)



for n in range(200):
    bob.pensize(3)
    bob.color(n,n,n)
    bob.circle(n)
    bob.right(135)


for times in range(200):
    bob.pensize(6)
    bob.color(255,255,255)
    bob.forward(times*5)
    bob.right(234)
    bob.left(334)

turtle.done              

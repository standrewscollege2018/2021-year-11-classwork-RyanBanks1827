#This code should do something awesome- It will Begin Turtle, And begin drawing a complex polygon#
FdVal=2
AngVal=0.1

import turtle
turtle.hideturtle()
turtle.speed(10)
while(True):
    turtle.forward(FdVal)
    turtle.right(AngVal)
    FdVal=FdVal+0.8
    AngVal=AngVal+0.4

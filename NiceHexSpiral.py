#NiceHexSpiral.py
import turtle
colors= ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(480):
    t.pencolor(colors [x%20])
    t.width(x/100+1)
    t.forward(x)
    t.left(20)

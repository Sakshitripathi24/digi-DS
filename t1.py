from turtle import *

speed('slowest')
#polygon
distance = 100
sides = 6

for i in range(sides):
    pencolor('red')
    fd(distance)
    rt(360/sides)
    circle(distance/2)
    for i in range(sides):
        pencolor('blue')
        rt(360/sides)
        pencolor('green')
        fd(distance/4)
        rt(360/sides)
        dot(10)
        write(i)
    
hideturtl()
mainloop() #this line is needed keep the window open
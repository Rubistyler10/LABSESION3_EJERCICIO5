from turtle import *

p = Screen()
p.setup(1000,800)
p.setup(990,790)


trotu = Turtle()
trotu.speed(8)
trotu.circle(50)
trotu.penup()
trotu.forward(100)
trotu.pendown()
trotu.circle(50)
trotu.penup()
trotu.left(90)
trotu.forward(100)
trotu.pendown()
trotu.forward(200)
trotu.left(90)
trotu.forward(100)
trotu.left(90)
trotu.forward(200)
trotu.penup()
trotu.goto(50,300)
trotu.left(90)
trotu.forward(50)
trotu.left(90)
trotu.pendown()
trotu.circle(50,extent = 180)
trotu.penup()
trotu.goto(0,-20)
trotu.pendown()
trotu.hideturtle()
trotu.write('POR SI TE ENTRA HAMBRE')





p.exitonclick()

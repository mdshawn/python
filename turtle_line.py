import turtle

turtle.shape('arrow')
turtle.speed(1)
turtle.color('blue')

for i in range(200):
    turtle.pendown()
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)
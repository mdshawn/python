import turtle

turtle.shape('turtle')
turtle.speed(1)
turtle.color('red')
turtle.penup()

height = 10
width = 10

for y in range (height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(width*20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
turtle.exitonclick()
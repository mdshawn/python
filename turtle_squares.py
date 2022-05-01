import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.color('red')
num = 0
while num <= 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    num += 1
turtle.exitonclick()

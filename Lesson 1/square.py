import turtle, random

colors = ["red", "orange", "white", "green", "blue", "pink", "purple", "yellow"]
storona = 20


t = turtle.Pen()
t.width(3)
turtle.speed(150)
turtle.bgcolor("black")
square = int(turtle.numinput("Количество квадратов", "Сколько квадратов нарисовать?",4, 1, 360))
for i in range(square):
    rnd_color = random.choice(colors)
    t.pencolor(rnd_color)
    for x in range(4):
        t.forward(storona)
        t.left(90)
    t.left(360/square)
    storona +=5

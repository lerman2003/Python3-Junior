import turtle, random

colors = ["red", "orange", "white", "green", "blue", "pink", "purple", "yellow"]
radius = 50


t = turtle.Pen()
t.width(3)
turtle.speed(0)
turtle.bgcolor("black")
circles = int(turtle.numinput("Количество окружностей", "Сколько окружностей нарисовать?",4, 1, 360))
for i in range(circles):
    t.pencolor(random.choice(colors))
    t.circle(radius)
    t.left(360/circles)
    radius +=5

import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.color("red")
t.width(3)
polygon=int(turtle.numinput("Количество многоугольников", "Сколько раз нарисовать многоугольники?",4, 1, 300))
kolst=int(turtle.numinput("Количество сторон", "Сколько сторон задать многоугольнику?",4, 3, 250))
for x in range(polygon):
    for i in range(kolst):
        t.forward(100)
        t.left(360/kolst)
    t.left(360/polygon)









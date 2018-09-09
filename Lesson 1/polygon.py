import turtle, random
t=turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "green", "blue", "pink", "purple", "yellow"]

storona = int(turtle.numinput("Количество сторон", "Сколько сторон у Вашего многоугольника?",4, 3, 360))
povtor = int(turtle.numinput("Количество повторений", "Сколько раз нарисовать многоугольники?",4, 1, 360))
t.pencolor(random.choice(colors))
for x in range(povtor):
    t.pencolor(random.choice(colors))
    for i in range(storona):
        t.forward(100)
        t.left(360/storona)
    t.left(360/povtor)
    

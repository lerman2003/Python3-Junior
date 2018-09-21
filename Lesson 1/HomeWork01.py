import turtle
t = turtle.Pen()
t.color("red")
t.width(3)
turtle.bgcolor("black")
trio=int(turtle.numinput("Количество треугольников","Сколько треугольников нарисовать?",6,1,101))
storona=int(turtle.numinput("Длина стороны","Какую длинну вы хотите задать?",50,1,1001))
for i in range(trio):
    for i in range(3):
        t.forward(storona)
        t.left(120)
    t.left(360/trio)









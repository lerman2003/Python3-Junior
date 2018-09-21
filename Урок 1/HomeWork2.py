import turtle
t = turtle.Pen()
t.color("red")
t.width(3)
turtle.bgcolor("black")
circle=int(turtle.numinput("Количество кругов","Сколько кругов нарисовать?",6,1,360))
radius=int(turtle.numinput("Радиус круга","Какой радиус вы хотите задать?",50,1,100))
for i in range(circle):
    t.circle(radius)
    t.left(360/circle)
    









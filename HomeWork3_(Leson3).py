import math
#Вступление
print("Решение квадратичных уравнений")
print("--------------")
#Ввод значений a,b,c (пользователем)
a = float(input("Введите значение а: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение с: "))
#Выполнение логческой задачи
d = (b**2)-4*a*c
if d>=0:
    print("--------------")
    print("Имеет корни")
else:
    print("--------------")
    print("Не имеет корней")


r = float(input("Ведите радиус круга: "))
a = float(input("Введите длину стороны квадрата: "))
print("------------")
#Вычисления площадей
s1 = r**2*3.14
s2 = a**2
#Завершающие вычесления и ответ
if s1<s2:
    print("Площадь квадрата больше")
else:
    print("Площадь круга больше")

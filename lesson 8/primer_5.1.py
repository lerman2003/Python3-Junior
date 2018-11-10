n = int(input('Введите натуральное число '))
Max = -1
#Рассматриваем все цифры
while n > 0:
    posl = n % 10
    if posl > Max:
        Max = posl
    n = n//10
print('Максимальная цифра заданного числа равна', Max)

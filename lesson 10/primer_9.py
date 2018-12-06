#Дана строка. Определить, образует ли число подстрока, начинающаяся с символа номер nach и заканчивающаяся символом номер kon.

st = input('Введите строку символов ')
nach = int(input('Введите номер начального символа подстроки '))
kon = int(input(' Введите номер конечного символа подстроки '))
if st[nach - 1 : kon - 1].isdigit():
	print('Да ...')
else:
	print('Нет …')
  
#без использования метода isdigit()
#Формируем подстроку, используя срез
podst = st[nach - 1 : kon]
eto_zifra = True
for sim in podst:
	if ord(sim) < 48 or ord(sim) > 57:
		eto_zifra = False
if eto_zifra == True: #Или if eto_zifra:
	print('Да ...')
else:
	print('Нет …')

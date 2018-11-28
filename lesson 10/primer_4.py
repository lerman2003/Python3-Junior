#Определить, является ли символ строки с заданным номером цифрой.

st = input('Введите строку ')
nom = int(input('Введите номер символа этой строки '))
nom = nom – 1

#способ 1
if (st[nom] == '0' or st[nom] == '1' or st[nom] == '2'
		or st[nom] == '3' or st[nom] == '4' or st[nom] == '5'
		or st[nom] == '6' or st[nom] == '7' or st[nom] == '8'
		or st[nom] == '9'):
	print('Да, этот символ - цифра')
else:
	print('Нет, этот символ цифрой не является')
  
#способ 2
if ord(st[nom]) >= 48 and ord(st[nom]) <= 57:
	print('Да ...')
else:
	print('Нет …')
  
#способ 3
vse = '0123456789'
if st[nom] in vse:
	print('Да ...')
else:
	print('Нет …')
  
 #способ 4
if st[nom].isdigit(): 		
	print('Да ...')
else:
	print('Нет …')

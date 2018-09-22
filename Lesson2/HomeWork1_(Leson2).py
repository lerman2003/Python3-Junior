suma=float(input("Сума заказа?")) 
tea=float(input("Сколько чая дадите нашим официантам?(Общее число)"))
people=int(input("Сколько вас(количество человек)"))
sumageneral=suma+tea
suma2=suma/people
sumaeach1=suma/people+tea/people
teaeach=tea/people
prozentsuma=suma/100
prozenttea=tea/prozentsuma
print("---------------------")
print("Чек:")
print("Сумма заказа",suma)
print("Чай(общий)",tea,"в процентах от заказа",prozenttea,"%")
print("Чай с каждого",teaeach)
print("Cумма для каждого (без чая)",suma2)
print("Cумма для каждого(вместе с чаем)",sumaeach1)
print("---------------------")
print("Итог(сумма заказа и чай)",sumageneral)
print("Мы рады что вы выбрали наш ресторан приходите к нам еще")

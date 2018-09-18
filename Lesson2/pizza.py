#pizza
#спросить о количестве пицц
number_of_pizza = int(input("Сколько пицц Вы хотите заказать? "))
#запросить стоимость пиццы
cost_per_pizza = float(input("Сколько стоит пицца? "))
#подсчитать стоимость каждой пиццы как подытог
subtotal = number_of_pizza*cost_per_pizza
#налог 8%
tax_rate = 0.08
sales_tax = subtotal*tax_rate
#итоговая стоимость
total = subtotal+sales_tax
print("Полная стоимость: ",'%.2f' % total," руб.")
print("В том числе ", '%.2f' % subtotal," руб. за пиццу и ")
print('%.2f' % sales_tax, " руб. - налог с продаж.")

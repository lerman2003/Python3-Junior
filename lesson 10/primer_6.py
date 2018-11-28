#Определить, сколько раз в заданной строке встречается некоторая подстрока.

#Способ 1

...
k = st.count(podst)
....

#Способ 2

st = input('Введите строку ')
podst = input('Введите подстроку ')
dlina1 = len(st)
dlina2 = len(podst)
k = 0
for nach in range(dlina1 - dlina2 + 1):
	if st[nach : nach + dlina2] == podst:
		k = k + 1
print(k)

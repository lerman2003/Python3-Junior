from random import randint
n_comp=randint(1,100)
print("угадай, какое число загадал компьютер")
k=0
while True:
    k+=1
    otvet=int(input("предположи число "))
    if otvet>n_comp:
        print("загаданное число меньше вашего")
    elif otvet<n_comp:
        print("загаданное число больше вашего")
    else:
        print("вам понадобилось", k, " попыток, чтобы угадать число")

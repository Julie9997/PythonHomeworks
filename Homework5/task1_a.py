# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

import random

total = 120
while total > 0:
    print('Всего конфет: ' + str(total))
    taken_h = -1
    while taken_h < 0 or taken_h > 28 or taken_h > total:
        taken_h = int(input('Ход человека: '))
        if taken_h > 28 or taken_h > total:
            print('Введите корректное число конфет')
    total -= taken_h
    if total == 0 :
        print('Человек победил!!!')
        break
    print('Всего конфет: ' + str(total))
    taken_b = 150
    while taken_b > total:
        taken_b = random.randint(1, 29)
    print('Ход бота: ' + str(taken_b))
    total -= taken_b
    if total == 0 :
        print('Бот победил!!!')
        break
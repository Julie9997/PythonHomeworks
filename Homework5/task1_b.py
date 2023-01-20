import random

def brain(total, candies):
    if candies == 1:
        n = random.randint(1, 29)
    else:
        n = 30 - candies
    if total <= 28:
        n = total
    return n

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
    taken_b = brain(total, taken_h)
    print('Ход бота: ' + str(taken_b))
    total -= taken_b
    if total == 0 :
        print('Бот победил!!!')
        break
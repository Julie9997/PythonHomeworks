# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

import random

n = int(input('n = '))
list = []
for i in range(n):
    list.append(random.randint(1, 10))
print(list)

summ = 0
for i in range(1, len(list), 2):
    summ += list[i]
print(f'Сумма чисел, стоящих на нечетных позициях: {summ}')
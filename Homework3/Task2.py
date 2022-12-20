# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n = int(input('n = '))
list = []
for i in range(n):
    list.append(int(input(f'{i}й элемент списка: ')))
print(list)

muls = []
if n % 2 == 0:
    for i in range(len(list)//2):
        muls.append(list[i] * list[-i-1])
else:
    for i in range(len(list)//2 + 1):
        muls.append(list[i] * list[-i-1])
print(muls)
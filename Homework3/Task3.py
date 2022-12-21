# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

n = int(input('n = '))
list = []
for i in range(n):
    list.append(float(input(f'{i}й элемент списка: ')))
print(list)

newList = []
for i in list:
    if i % 1 != 0:
        newList.append(round(i % 1, 2))
        
print(newList)
differ = max(newList) - min(newList)
print('Разница между максимальным и минимальным значением дробной части элементов:', round(differ, 2))
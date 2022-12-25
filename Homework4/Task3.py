# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

lst = list(map(int, input('Последовательность чисел: ').split()))
unique_list = []
count = 0
for i in lst:
    for j in lst:
        if i == j:
            count += 1
    if count == 1:
        unique_list.append(i)
    count = 0

print(*unique_list, sep=' ')
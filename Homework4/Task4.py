# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 

# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

#     a, b, c, d, e, h - рандом

import random

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }


def degree(n):
    degrees = ""
    s = str(n)
    for char in s:
        degrees += indexes[char] or ""
    return degrees
    

koef_list = []

k = int(input('k = '))

for i in range(k + 1):
    koef_list.append(random.randint(0, 100))

el_list = []
el_list.append(str(koef_list[0]))
el_list.append(str(koef_list[1]) + 'x')
for i in range(2, k+1):
    st = degree(i)
    y = str(koef_list[i]) + 'x' + st
    el_list.append(y)

print(*reversed(el_list), sep=' + ')
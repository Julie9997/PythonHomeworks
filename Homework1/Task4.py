# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quater = int(input('Номер четверти: '))

if quater == 1:
    print('x ∈ (0; +∞)')
    print('y ∈ (0; +∞)')
if quater == 2:
    print('x ∈ (-∞; 0)')
    print('y ∈ (0; +∞)')
if quater == 3:
    print('x ∈ (-∞; 0)')
    print('y ∈ (-∞; 0)')
if quater == 4:
    print('x ∈ (0; +∞)')
    print('y ∈ (-∞; 0)')
else:
    print('Неверный номер четверти')
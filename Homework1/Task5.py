# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

print('Координаты первой точки:')
x1 = float(input('x = '))
y1 = float(input('y = '))
print('Координаты второй точки:')
x2 = float(input('x = '))
y2 = float(input('y = '))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f'Расстояние: {round(distance, 2)}')
 
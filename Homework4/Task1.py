# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь
import math

n = int(input('Введите количесиво знаков послле запятой: '))
 
pi = math.pi

print("{:.{precision}f}".format(pi, precision=n))
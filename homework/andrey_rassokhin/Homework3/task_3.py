# Даны два числа.Найти среднее арифметическое \n и среднее геометрическое этих чисел
import math

num_1 = 2
num_2 = 4
arithmetic_mean = (num_1 * num_2) / 2
geometric_mean = math.sqrt(num_1 * num_2)
print(f' Среднее арифметическое = {arithmetic_mean} '
      f'\n Среднее геометрическое = {geometric_mean}')

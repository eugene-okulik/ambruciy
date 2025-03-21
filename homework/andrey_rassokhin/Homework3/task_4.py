# Даны катеты прямоугольного треугольника.Найти его гипотенузу и площадь
import math


a = 3
b = 4
hypotenuse = math.sqrt(a ** 2 + b ** 2)
square = 0.5 * a * b
print(f' Гипотенуза = {hypotenuse} \n Площадь треугольника = {square}')

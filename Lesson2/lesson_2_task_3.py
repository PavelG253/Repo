import math


def square(len):
    return math.ceil(area=len ** 2)


len = float(input("Введите длину стороны: "))

print(f"Площадь квадрата составляет: {math.ceil(len ** 2)}")

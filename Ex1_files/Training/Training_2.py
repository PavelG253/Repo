'''
age = 18

print(age < 18)

if age < 18:
    print("Б/а напитки в другом отделе")
if age >= 18:
    print("Пей, что хочешь")
#else:
 #   print("Пей, что хочешь!")
'''

#for x in range(1,21):
 #   print("x=",x, "x²=",x*x)

'''
students = ["Александр", "Кирилл", "Филипп", "Михаил", "Мирон", "Ольга", "Виктор"]
'''
'''
l=len(students)
for i in range(0,l):
    print(students[i])
'''
'''
for student in students:
    print(student)
'''
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    if (n % 2 == 1):
        print(n)
'''
'''
user_login = "adam"
user_password = "eva"

login = input("Login: ")
password = input("Password: ")

if (login == user_login) and (password == user_password):
    print("Secret is open")
else:
    print("There is nothing interesting here")
'''

'''
crit1 = "red"
crit2 = "lock"

color = input("What colour do you prefer? ")
feature = input("What features are you interested in? ")

if (color == crit1) or (feature == crit2):
    print("Buy it!")
else:
    print("I'm looking for smth special")
'''

'''
Дан список 
employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
Выведите на экран второй и второй с конца элементы через запятую. Продумайте такое решение, которое можно было бы применить к списку любой длины.


employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
print(employee_list[1], employee_list[-1])
'''


'''
Создайте функцию 
dev_by_three
, которая принимает один аргумент — число — и возвращает 
'Да'
, если оно делится на три, и 
'Нет'
 — если не делится.
В этом же файле напишите код, который вызывает функцию и передает в нее число.
Результат вызова функции должен сохраняться в переменную.
Выведите в консоль сообщение в формате: 
Делится ли на три <число>? - Нет | Да.



def div_by_three(num):
    return "Да" if num % 3 == 0 else "Нет"


num = int(input("Введите число: "))


result = div_by_three(num)
print(f"Делится ли на три {num}? - {result}")
'''


'''
Напишите функцию 
min_boxes
, которая принимает одно число — количество предметов — и возвращает минимальное количество коробок, необходимых для упаковки этих предметов, если в одну коробку помещается не более пяти предметов.
Используйте функцию 
ceil
 из модуля 
math
, чтобы округлить количество коробок до ближайшего целого числа вверх.


import math


def min_boxes(items):
    return math.ceil(items/5)


num_items = int(input("Введите количество предметов: "))


print(f"Минимальное количество коробок: {min_boxes(num_items)}")
'''

'''
Напишите функцию 
check_divisibility
, которая принимает одно число — 
n
 — и выводит все числа от 1 до 
n
 (включительно):
Если число делится на 2, но не на 4, оно выводится с текстом «Делится на 2, но не на 4».
Если число делится и на 2, и на 4, оно выводится с текстом «Делится и на 2, и на 4».
Все остальные числа выводятся просто как есть.
'''

n = int(input("Введите число: "))
      
      
def check_divisibility(n):

    for i in range(1, n+1):
        if i % 4 == 0:
            print(f"{i} - Делится и на 2, и на 4")
        elif i % 2 == 0:
            print(f"{i} - Делится на 2, но не на 4")
        else:
            print(i)


check_divisibility(n)



'''
Напишите функцию 
quarter_of_year()
, которая принимает один аргумент — номер месяца (от 1 до 12) — и возвращает номер квартала, к которому относится этот месяц.
Например, если передать 5, на выходе должно быть 
II квартал
, так как май относится ко второму кварталу.


def quarter_of_year(month):
    if 1<=month<=3:
        return "I квартал"
    elif 4<=month<=6:
        return "II квартал"
    elif 7<=month<=9:
        return "III квартал"
    elif 10<=month<=12:
        return "IV квартал"
    else:
        return "Неверный номер месяца"
    

try:
    month=int(input("Введите номер месяца: "))
    print (quarter_of_year(month))
except ValueError:
    print("Пожалуйста, введите правильный номер месяца от 1 до 12.")
'''


'''
Дан список 
lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
.
Необходимо вывести элементы, которые одновременно:
больше 15,
делятся на 3 без остатка.

lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
result = [x for x in lst if x > 15 and x % 3 ==0]
print(result)
'''


'''
Создайте список 
[25, 20, 15, 10, 5]
 с помощью функции 
range()
 и выведите его на экран.

for i in range(25,0,-5):
    print(i, end=' ')

my_list = list(range(25, 0, -5))
print(my_list)
'''


'''
Создайте переменные:
var_1 = 50
var_2 = 5
Напишите код, который меняет значение переменных местами (
var_1
 должен быть равен 5, а 
var_2
 — 50).
Выведите обновленные переменные на экран.


var_1 = 50
var_2 = 5

temp = var_1
var_1 = var_2
var_2 = temp

print("var_1 =", var_1)
print("var_2 =", var_2)

#or

var_1 = 50
var_2 = 5

var_1, var_2 = var_2, var_1

print("var_1=", var_1)
print("var_2", var_2)
'''
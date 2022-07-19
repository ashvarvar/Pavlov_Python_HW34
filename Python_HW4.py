### 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi
# Формула Бэйли — Боруэйна — Плаффа
d =  int(input("Введите число для заданной точности числа Пи:\n"))
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(d))

print(f'число Пи с заданной точностью {d} равно {round(my_pi, d)}')

###====================================================================================
### 2- Задайте последовательность чисел. Напишите программу, 
###которая выведет список неповторяющихся элементов исходной последовательности.
###Посмотрели, что такое множество? Вот здесь его не используйте.

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 5
m = 1
n = 9

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))

###=============================================================================
### 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
### Пример: при N = 12 -> [2, 3]
number = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
num = number
while i <= number:
    if number % i == 0:
        lst.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {num} приведены в списке: {lst}")
###===================================================================================
### 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
### В файле содержится, например:
### Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
text = "Мама сшила м0не штаны и7з бере9зовой кор45ы 893"
import re
items = [word for word in text.split() if not re.search('\d', word)]
print(items)


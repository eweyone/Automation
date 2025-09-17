# Задача 1. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
from itertools import count


def two_numbers(a, b):
    if a > b:
        print(a)
    else:
        print(b)

two_numbers(15, 10)


# Задача 2. Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”
def two_nums(c, d):
    if c - d == 135 or c - d == -135:
        print('yes')
    elif d - c == 135 or d - c == -135:
        print('yes')
    else:
        print('no')

two_nums(-100, 35)


# Задача 3. Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)
def month(m):
    if m in range(1, 3) or m == 12:
        print('Зима')
    elif m in range(3, 6):
        print('Весна')
    elif m in range(6, 9):
        print('Лето')
    elif m in range(9, 12):
        print('Осень')
    else:
        print('Введите корректный месяц(1-12)')

month(9)


# Задача 4. Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”
def three_numbers(z, x, c):
    if z > 10 and x > 10 and c > 10:
        print('yes')
    else:
        print('no')

three_numbers(11, 11, 11)


# Доп. Задача 1. Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.
def the_list(f:list):
    count = 0
    for element in f:
        if element > 0:
            count = count + 1
    return count

print(the_list([1, -2, -3, -4, 5]))


# Доп. Задача 2. Функция на вход получает 2 переменные.
# a. Кол-во лет (int)
# b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
def years_and_months(j:int, k:int):
    years = j * 12 * 29
    months = k * 29
    return years + months

print(years_and_months(1, 6))
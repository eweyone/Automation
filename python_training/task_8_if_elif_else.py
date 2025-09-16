num = 3

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('Да')
    else:
        print('Нет')

task_yes_no('test', 'test1')


num_float = -4.5
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


# permit_print = False
permit_print = True
num_1 = 5

if num_1 > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


# Напишите программу, которая отвечает какое Ваше текущее звание исходя из курса.
# Варианты званий:
# бакалавр - 1-4 курс (включительно)
# магистр - 5-6 курс (включительно)
# аспирант - 7-9 курс (включительно)
# если введенное число не соответствует ни одному диапазону, вывести:"Введите корректный год обучения"

def student_course(y_o_study):
    if y_o_study == 1 or y_o_study == 2 or y_o_study == 3 or y_o_study == 4:
        print('Вы - бакалавр')
    elif y_o_study in range(5, 7): # 7 не будет включено
        print('Вы - магистр')
    elif 7 <= y_o_study <= 9:
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student_course(12)


# если число больше 100 или меньше -100, вывести "-"б иначе вывести "+"
def number(numb):
    if numb > 100 or -100 < numb:
        print('-')
    else:
        print('+')

number(-993)
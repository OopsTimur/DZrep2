# Senko_Timur group_208
# DZ
import math


# 1. Напишите функцию, которая принимает на вход два аргумента и возвращает их сумму.

def f(a, b):
    return a + b


print(f(1, 2))


# 2. Напишите функцию, которая принимает на вход список чисел и возвращает их среднее значение.


def mid_summ():
    c = 0
    s = 0
    for i in range(1, 25 + 1):
        s += i
        c += 1
    mid_znach = s / c
    print(s)  # Для оценки правильного ответа)
    print(mid_znach)


mid_summ()


# 3. Напишите функцию, которая принимает на вход число и возвращает True, если оно четное, и False, если оно нечетное.

def even_odd():
    c = int(input())
    if c % 2 == 0:
        print('True')
    else:
        print('False')


even_odd()


# 4. Напишите функцию, которая принимает на вход список и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def individual_list():
    b = []
    while True:
        a = input('Введите число, если хотите остановить нажмите n:')
        if a == 'n':
            break
        b.append(a)
    print(set(b))


individual_list()


# 5. Решите задачу с использованием вложенной функции is_square. Предположим, у нас есть список чисел и мы хотим
# найти все числа, которые являются квадратами других чисел в этом списке. Шаблон кода (ориентировачный):

def sss_square():
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 81, 64, 128, 225, 100, 10, 10000]
    c = []

    def is_square(x):
        return x ** 2 in b

    for i in b:
        if is_square(int(i)):
            c.append(i)
        else:
            continue
    print(c)


sss_square()

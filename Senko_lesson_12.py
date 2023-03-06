# Senko Timur (group_208)
# DZ
# 1. Написать рекурсивную функцию, которая определяет, является ли строка палиндромом
# (одинаково читается в обе стороны: герег, лол, мам, level и тд.)
# Шаблон:
# def is_palindrome(stroka):
#     if len(stroka) < 2:
#         return True
#     elif stroka[0] != stroka[-1]:
#         return False
#     else:
#         return is_palindrome('')
#
#
# print(is_palindrome('шалаш'))


# 2. Написать рекурсивную функцию для подсчета количества элементов в списке.
def recursion_sum(arr):
    if not arr:
        return 0
    else:
        return arr[1] + recursion_sum(arr[1:])


print(recursion_sum([1, 2, 3, 4, 5, 6]))
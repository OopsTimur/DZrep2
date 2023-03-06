# Senko Timur (group_208)
# DZ


# 1. Написать рекурсивную функцию, которая определяет, является ли строка палиндромом
# (одинаково читается в обе стороны: герег, лол, мам, level и тд.)
# Шаблон:

def is_palindrome(stroka):
    if len(stroka) < 2:
        return True
    elif stroka[0] != stroka[-1]:
        return False
    else:
        return is_palindrome('')


print(is_palindrome('шалаш'))


# 2. Написать рекурсивную функцию для подсчета количества элементов в списке.

def recursion_sum(arr):
    s = []
    if len(arr) > 0:
        return 1 + recursion_sum(arr[1:])
    else:
        return 0


print(recursion_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))



#3. Этот код отсортирует список строк по последнему символу в каждой строке.
    # Здесь использована лямбда-функция в качестве ключа в сортировке.
    # Измените код так, чтобы сортировка была по второму символу каждой строки

strings = ['apple', 'banana', 'cherry', 'date', 'account', 'Ibicca']
sorted_strings = sorted(strings, key=lambda s: s[1])
print(sorted_strings) # Output: ['cherry', 'date', 'apple', 'banana'] # Добавил слов, чтобы проверить, всё ли правильно



#4. Напишите функцию make_adder(n),
# которая принимает целое число n и возвращает внутреннюю функцию,
# которая может прибавлять этот n к любому другому целому числу.

def make_adder(n):
    def summa(s):
        return n+s
    return summa

print(make_adder(5)(2))



#5. Напишите функцию counter(), которая возвращает внутреннюю функцию increment(),
# которая увеличивает счетчик на 1 каждый раз, когда она вызывается.


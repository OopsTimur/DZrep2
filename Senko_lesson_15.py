# Senko_Timur 208_group
# DZ


class math:
    first_2 = input('Введите число: ')
    while not first_2.isdigit():
        print('Неправильно число!')
        first_2 = input('Введите число: ')
    first_2 = float(first_2)
    second_2 = input('Введите второе число: ')
    while not second_2.isdigit():
        print('Неправильно число!')
        second_2 = input('Введите второе число: ')
    second_2 = float(second_2)
    operation_2 = input('Введите операцию: ')

    def while_2(self):
        while True:

            if self.operation_2 == '+':
                def plus():
                    return self.first_2 + self.second_2
                return plus()

            if self.operation_2 == '-':
                def minus():
                    return self.first_2 - self.second_2
                return minus()

            if self.operation_2 == '*':
                def multiply():
                    return self.first_2 * self.second_2
                return multiply()

            if self.operation_2 == '/':
                def div():
                    try:
                        return self.first_2 / self.second_2
                    except ZeroDivisionError: print('На ноль делить нельзя!')
                return div()

            if self.operation_2 == 'n':
                break


calculator = math()
print(calculator.while_2())

# Senko_Timur 208_group
# DZ


class math:
    def __init__(self, first, second, operation):
        self.first_2 = float(first)
        self.second_2 = float(second)
        self.operation_2 = operation

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


calculator = math( input('Введите первое число: '), input('Введите второе число: '), input('Введите операцию: '))
print(calculator.while_2())

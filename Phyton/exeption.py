a = int(input('Введите первое значение: '))
b = int(input('Введите втрое значение: '))

try:
    result = a / b
    print('Результат: ', int(result))
except ZeroDivisionError:
    result = False
    print('Делить на ноль нельзя. Результат: ', result)
# print('Результат: ', int(result))

from opers import opss
a = opss.input_number('Введите первое число (a): ')
b = opss.input_number('Введите второе число (b): ')
zn = opss.input_znak('Введите арифметический знак, один из: +, -, *, / ')
if zn == '+':
    opss.sums(a, b)
elif zn == '-':
    opss.sub(a, b)
elif zn == '/':
    try:
        opss.dev(a, b)
    except ZeroDivisionError:
        result = False
        print('Делить на ноль нельзя')
elif zn == '*':
    opss.mult(a, b)

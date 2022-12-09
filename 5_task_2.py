# Задача 2 Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

a = float(input('Введите число: '))
b = input('Выберите действие: "+", "-", "*", "/" ')
c = float(input('Введите число: '))
if b == '+':
    print(a + c)
if b == '-':
    print(a - c)
if b == '*':
    print(a * c)
if b == '/':
    try:
        answer = a / c
    except ZeroDivisionError:
        answer = "Деление на 0!"
    print(answer)
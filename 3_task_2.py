# task № 2
# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точностью 3
# Вариант № 1. Среднее арифмитическое для целых чисел
print('Введите три целых числа')
a = input('Первое число: ')
b = input('Второе число: ')
c = input('Третье число: ')
s = (int(a) + int(b) + int(c))/3
print(round((int(a) + int(b) + int(c))/3, 3))

# Вариант № 2. Среднее арифмитическое для дробных чисел
print('Введите три дробных числа')
a = input('Первое число: ')
b = input('Второе число: ')
c = input('Третье число: ')
s = (float(a) + float(b) + float(c))/3
print(round((float(a) + float(b) + float(c))/3, 3))

# ?! Вариант № 3. По идее должен давать такой же результат что и Вариант № 2.
# Но результат разный. В чём ошибка?

# print('Введите три дробных числа')
# a = float(input('Первое число: '))
# b = float(input('Второе число: '))
# c = float(input('Третье число: '))
# s = (a + b + c)/3
# print(round(s/3, 3))
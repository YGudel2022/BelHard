# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# функция, которая проверяет числа на нечетность
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False
# Удаление нечетных чисел с помощью filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)
print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))








# n = int(input("Введите n: "))
# for i in range(2, n+1):
#     if i%2 == 0:
#         print(i)

# n = int(input())
# c = 5
# for i in range(1, n+1):
#     print(i, end='\n' if i else ', ' if (i % 5) else ',\n')

# a = float(input('Введите число: '))
# b = input('Выберите действие: "+", "-", "*", "/" ')
# c = float(input('Введите число: '))
# if b == '+':
#     print(a + c)
# if b == '-':
#     print(a - c)
# if b == '*':
#     print(a * c)
# if b == '/':
#     try:
#         answer = a / c
#     except ZeroDivisionError:
#         answer = "Деление на 0!"
#     print(answer)

# number = 55.
# # Выполняем проверку условия
# if number < 15:
#     # Если условие True
#     print("Переменная number < 15")
# else:
#     print("Переменная number > 15")

# # Объявляем переменные
# number_1 = 10
# number_2 = 10
#
# # Выполняем проверку условия
# if number_1 == number_2:
#     # Если условие if - True
#     print("Число number_1 равно числу number_2")
# elif number_1 > number_2:
#     # Если условие elif - True
#     print("Число number_1 больше числа number_2")
# elif number_1 < number_2:
#     # Если условие elif - True
#     print("Число number_1 меньше числа number_2")
# else:
#     # Если условия if и elif - False
#     print("Число number_1 не равно числу number_2")
# # Финальный результат в консоли

# x = 5
# while x <= 10:
#     print(x)
#     x = x+3

# x = 1
# while x <= 3:
#     print(x)
#     x = x + 1
# else:
#     print("Готово")

# x = 1
# while x <= 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1

# x = 1
# while x <= 10:
#     if x == 5:
#         x += 1
#         continue
#     print(x)
#     x += 4



# # Запрашиваем у пользователя целое число
# x = int(input("Введите число: "))
# # Определяем, входит ли значение в число первых пяти простых чисел
# if x % 2 == 0:
#     print("zero")
# else:
#     print("Это нечёт")

# # Запрашиваем ввод у пользователя
# x = int(input("Введите целое число (0 для выхода): "))
# # Запускаем цикл, пока пользователь не введет ноль
# while x != 0:
#     if x > 0:
#         print("Это положительное число.")
#     else:
#         print("Это отрицательное число.")
#     x = int(input("Введите целое число (0 для выхода): "))

# text = input("Введите текст: ")
# text_replace = text.replace(" ", "") # удалил пробелы
# text_lower = text_replace.lower() # перевёл в нижний регистр
# print(dict((list_letters,text_lower.count(text_lower)) for list_letters in set(text_lower)))
# text = input("Введите текст: ")
# text_replace = text.replace(" ", "") # удалил пробелы
# text_lower = text_replace.lower() # перевёл в нижний регистр
# print ({n: text_lower.count(n) for n in text_lower})

# text = "jjjkoiu8TTTT"
# print(''.join(c for c in text if c.isupper()))

# a = [2, 4, 6, 22]
# while 2 in a:
#     a.remove(2)
#     print(a)

# text = input("введи число: ")
# while not text.isspace():
#     text = input("введи число: ")
#     print(text)

# print(sum([int(i) for i in list(str(int(input('a='))))]))

# numbers = input('a= ')
# s = 0
# for i in numbers:
#     s += int(i)
# print(f'{s=}')

# text = [2, 2, 22, 2222, 222, 33, 3, 4, 44, 444, 4, 2]
# print(set(text))
# for index, value in enumerate(text):
#     print(index, value)


# doc = ['sss', 'ddd', 'rrr', 'ttt']
# for index, value in enumerate(doc):
#     print(index, value)

# go = ['aaaaaa', 3333]
# for index, value in enumerate(go):
#     print(index, value)

# nambers = [i for i in range(1, 9)]
# print(nambers)

# nambers = [i%2 for i in range(4, 9)]
# print(nambers)

# text1 = ['rrrr', 'wwwww', '22222']
# text2 = ['rrrr', 'wwwww', '22222']
# text = text1 + text2
# sente = ''.join(text)
# print(sente)

# x = int(input(': '))
# if 6 < x < 17:
#     print('rrrr')
# else:
#     print('jjjjjj')

# x = input(': ')
# x = 2 * x
# print(x)

# text = ['rrrr', 'wwwww', '22222']
# text = text * 2
# sente = ''.join(text)
# print(sente)
# print(text)



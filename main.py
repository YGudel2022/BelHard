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

nambers = input('a= ')
s = 0
for i in numbers:
    s += int(i)
print(f'{s=}')
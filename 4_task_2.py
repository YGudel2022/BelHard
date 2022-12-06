# 4_task_2
# 2. Без использования collections, написать программу,
# которая будет создавать словарь для подсчитывания
# количества вхождений каждой буквы в текст введенный с клавиатуры

text = input("Введите текст: ")
text_replace = text.replace(" ", "") # удалил пробелы
text_lower = text_replace.lower() # перевёл в нижний регистр
print(dict((list_letters,text_lower.count(text_lower)) for list_letters in set(text_lower)))

# # С использованием collections
# line = list(input())
# from collections import Counter     # импортируем счетчик
# print(dict(Counter(line)))


# Без collections решить не удалось
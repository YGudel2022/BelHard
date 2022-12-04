# 4_task_2
# 2. Без использования collections, написать программу,
# которая будет создавать словарь для подсчитывания
# количества вхождений каждой буквы в текст введенный с клавиатуры

# С использованием collections
line = list(input())
from collections import Counter     # импортируем счетчик
print(dict(Counter(line)))


# Без collections решить не удалось
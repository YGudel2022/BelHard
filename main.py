                            # [:] – получаем весь список
                            # [start:] – от start до конца списка
                            # [:end] – от начала до (end – 1)
                            # [start:end] – от start до (end – 1)
                            # [start:end:step] – от start до (end – 1) из элементов, чье смещение
                            # кратно step

# numbers = [1, 2, 'hello', "world", 5]
# print(numbers[2])         # вызывает значение по индексу
# print(numbers[::2])       # вызывает список по указанным индексам
# numbers[2] = "NEW"        # добавляет в список значение на место индекса
# print(numbers)            # теперь список содержит новое значение
# print(numbers[2][1])      # вначале находит значение по [2] и в нем вызывает по индексу [1] значение
# print(len(numbers))       # длина списка - 5 элементов
# print(len(numbers[2]))    # длина элемента списка по индексу [2] из списка -> 5 символов
# print(list('hello'))      # преобразование с помощью функции list к типу список

# from random import randint #  создание списка с помощью List Comprehension
# numbers = [randint(1, 10) for i in range(10)] # [элемент for элемент in итерабельный объект]
# print(numbers)

# words = ['hello', 'python', 'world', 'python', 'pycharm']   # есть список
# words.remove('python')    # метод(или функция как в презентации???) .remove удаляет первый элемент,
                            # который равен переданному значению
# print(words)

# words = ['hello', 'python', 'world', 'python', 'pycharm']   # есть список
# print(words)
# del words[1]              # оператор del удаляет конкретный элемент по индексу
# print(words)

# words = ['hello', 'python', 'world', 'python', 'pycharm']   # есть список
# print(words)
# a = words.pop(2)            # метод .pop удаляет элемент по индексу из списка и возвращает его
#                             # Если индекс не будет указан, то удалится последний элемент
# print(words)
# print(a)                    # вызовет world


# numbers = [1, 2, 3, 4]
# numbers_1 = 5 in numbers        # проверить, есть ли элемент в списке, нужно
#                                 # воспользоваться оператором in:
# print(numbers_1)
# numbers_2 = 5 not in numbers    # Для обратной проверки, нет ли элемента в списке,
#                                 # нужно воспользоваться оператором not in:
# print(numbers_2)

# numbers = [1, 2, 3, 4]
# print(numbers)
# numbers.append('hello')         # функция .append добавляет (элемент) в конец списка
# print(numbers)
# numbers.insert(1, 'new')        # функция .insert добавляет элемент на конкретное место в списке
#                                 # Элемент вставляется на указанное место, а элемент, который был
#                                 # под этим индексом, а также последующие элементы смещаются на
#                                 # один
# print(numbers)

# numbers1 = [1, 2, 3, 4]
# numbers2 = [5, 6, 7, 8]
# numbers3 = numbers1 + numbers2 #можем складывать и умножать
# print(numbers1 * 3)
# print(numbers2)
# print(numbers3)

# numbers1 = [1, 2, 3, 4]
# print(numbers1)
# numbers2 = "hello"
# numbers1.extend(numbers2)         # Для объединение списка с каким-нибудь итерируемым объектом
#                                   # (например другая коллекция), необходимо воспользоваться
#                                   # функцией: .extend(iterable)
# print(numbers1)
# numbers3 = [1, 2, 3, 9, "hello"]
# numbers1.extend(numbers3)
# print(numbers1)

# numbers = [1, 2, 3, 4]
# some_numbers = numbers.index(3)     # чтобы узнать индекс элемента в списке по его значению,
#                                     # нужно воспользоваться функцией (можно вести поиск от индекса
#                                     # start до индекса end) .index
#                                     # Генерирует исключение ValueError, если элемента не существует
# print(some_numbers)

# numbers = [3, 2, 3, 4, 3, 3]
# some_numbers = numbers.count(1)         # сколько элементов в списке с некоторым
#                                         # значение, нужно воспользоваться функцией  .count(значение)
# print(some_numbers)

# numbers = [4, 8, 7, 5, 3, 6, 2, 1, ]
# numbers.sort(reverse=False)                  # Функция списка list.sort([key][, reverse]), которая сортирует
#                                             # текущий список, reverse=False по возрастанию
# print(numbers)

# numbers = [4, 8, 7, 5, 3, 6, 2, 1, ]
# numbers_sort = sorted(numbers)                 # Общая функция sorted(список[, key][, reverse]), которая
#                                                # возвращает отсортированную копию списка
# print(numbers)
# print(numbers_sort)                            # [1, 2, 3, 4, 5, 6, 7, 8]

# numbers = [4, 8, 7, 5, 3, 6, 2, 1, ]
# numbers_sort = sorted(numbers, reverse=True)        # [8, 7, 6, 5, 4, 3, 2, 1]
# numbers_sort1 = sorted(numbers, reverse=False)      # [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers)
# print(numbers_sort)
# print(numbers_sort1)

# numbers = ['hello', 'Python', 'apple', 'bread', 'World']
# numbers.sort() # лексическая сортировка, вначале заглавные
# print(numbers)

# numbers = ['hello', 'Python', 'apple', 'bread', 'World', [2, 5, 3, 6, 7]]
# numbers[5].sort() # сортировка по индексу, в нащем случае сортирует в [2, 5, 3, 6, 7]
# print(numbers) # результат ['hello', 'Python', 'apple', 'bread', 'World', [2, 3, 5, 6, 7]]

# numbers = [1, 2, 3, 4, 5]               # спиок
# numbers.reverse()                       # разворот reverse()
# print(numbers)                          # [5, 4, 3, 2, 1]
# numbers_reversed = numbers[::-1]        # обратная сортировка [::-1] (изменили порядок на обратный)
# print(numbers_reversed)                 # [1, 2, 3, 4, 5]
# numbers.clear()                         # очистили спиок .clear()
# print(numbers)                          # список пуст []

# numbers = []
# numbers = list()
# print(numbers)

# numbers = [1, 2, 3, 4]
# numbers2 = [numbers, 5, 6, 7]
# numbers2[0].append('new')             # добавили в конец списка 'new' => [1, 2, 3, 4, 'new']
# print(numbers)

# numbers = (1, 2, 3, 4, [5, 6, 7, 8])
# numbers[4].append(9) # добавили 9 по индексу [4] в конец [5, 6, 7, 8]
# numbers.count(2)    # ? зачем это здесь
# print(numbers)
# new_number = numbers + numbers * 3 # можно скадывать и умножать
# print(new_number)


# Так как кортеж по своей сути, это неизменяемый список, то работа
# с ним происходит аналогично, за исключение того, что невозможно
# применить методы, которые могут его изменить:
# del, remove, pop, append, insert
# extend, reverse, sort, clear

# words = {'hello', 'python', 'world', 'pycharm'} # КОРТЕЖ
# print(words)

# s = {i**2 for i in range(1, 10)}        # кортеж из квадратов чисел от 1 до 9
# print(s)
# s2 = {5, 3, 6, 8, 2, 5, 3, 6}           # в кортеже нет дубликатов
# print(s2)
# s1 = {3, 6, 5, 4}
# s2 = {8, 2, 6, 2, 0}
# s3 = {1, 2, 3, 4, 5, 9, 8, }
# s4 = s1 | s2 | s3                       # объединяет, удаляя дубликаты
# print(s4)

# Множество – изменяемая структура данных, которая содержит в
# себе уникальные значения
# Множество не упорядочено, следовательно у элементов нет
# индексов и нельзя взять срез
# Множество имеет длину (len)
# Можно проверить вхождение и не вхождение элемента (in/not in)

# Множество можно создать тремя способами:
# С помощью {перечисление_элементов}
# С помощью функции set()
# С помощью Set Comprehension, вида:
# {элемент for элемент in итерабельный объект}

# s1 = {1, 2, 3, 4, 5, 6, }
# s2 = {4, 5, 6, 7, 8}
# s4 = {5, 4, 8, 9}
# s3 = s1 & s2 & s4 # оставит из множеств только пересекающиеся значения, другие удалит
# print(s3)

# # Создали словарь {} - dict
# user = {
#     'name': 'vasya',
#     'age': 34,
#     'is_human': True
# }
# print(user['age']) # вызвали по ключу age число лет 34
# user['age'] = 23
# user['city'] = 'minsk' # изменили к-во лет на 23 и добавили новую пару ключ-значение 'city': 'minsk'
# print(user)

# user = [['name', 'vasya'], ['age', 23]]
# user = dict(user) # объявили словарь
# print(user.setdefault('city', 'Н/У')) # dict.setdefault(key[, default]) -
#                             # возвращает значение ключа, но если его нет,
#                             # не бросает исключение, а создает ключ со значением default (по умолчанию None)
# print(user)

# keys = ['name', 'age', 'city']
# user = dict.fromkeys(keys, None)        # создаём словарь Функция dict.fromkeys(keys[, value])
# print(user)                             # результат {'name': None, 'age': None, 'city': None}
# user = {
#     'name': 'vasya'
# }
# print(user.popitem())               # результат ('name', 'vasya')
#                                     # dict.popitem() - удаляет и возвращает пару (ключ, значение).
#                                     # Если словарь пуст, бросает исключение KeyError.
#                                     # Помните, что словари неупорядочены.
# print(user)                         # Результат {} - ПОЧЕМУ?
# age = user.pop('age', None)         # dict.pop(key[, default]) - удаляет ключ и возвращает значение.
#                                     # Если ключа нет, возвращает default (по умолчанию бросает
#                                     # исключение).
# print(age)                          # результат None
# user = {
#     'name': 'vasya',
#     'age': 23
# }
# user2 = {
#     'age': 32,
#     'city': 'minsk'
# }
# # user.update(user2)
# user3 = user | user2
# print(user3)                        # результат {'name': 'vasya', 'age': 32, 'city': 'minsk'}


# numbers = (7, 4, 6, 2, 8, -12, -56, 3, 4)
# numbers2 = [5, 6, 3, 5, 3]
# print(min(numbers))
# print(sum(numbers))
# words = ['hello', 'python', 'world', 'hell', 'Apply', 'app']
# print(min(words))

from collections import Counter, deque, namedtuple, ChainMap

# text = 'hello world'
# text2 = 'python'
# count = Counter(text)
# count2 = Counter(text2)
# print(list(count.elements())) # ['h', 'e', 'l', 'l', 'l', 'o', 'o', ' ', 'w', 'r', 'd']
# print(count.most_common(2)) # [('l', 3), ('o', 2)]
# print(count) # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# print(count2) # Counter({'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1})
# count.subtract(count2)
# print(count) # Counter(
    # {'l': 3, 'e': 1, 'o': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, 'h': 0, 'p': -1, 'y': -1, 't': -1, 'n': -1})
# text = 'hello'
# data = {i: i for i in text}
# print(data) # {'h': 'h', 'e': 'e', 'l': 'l', 'o': 'o'}

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# q = deque(numbers, 4 // 2)
# print(q) # deque([9, 0], maxlen=2)

# keys = ['name', 'age', 'city']
# User = namedtuple('User', keys)
# vasya = User('vasya', 23, 'minsk')
# petya = User('petya', 32, 'brest')
# print(vasya.name) # vasya
# print(petya.age) # 32
# print(vasya._asdict()) # {'name': 'vasya', 'age': 23, 'city': 'minsk'}

# data1 = {
#     'a': 1,
#     'b': 2
# }
# data2 = {
#     'b': 3,
#     'c': 4
# }
# chain = ChainMap(data1, data2)
# # data1['c'] = 5
# print(chain['c']) # 4
# chain['e'] = 6
# print(data1) # {'a': 1, 'b': 2, 'e': 6}
# print(data2) # {'b': 3, 'c': 4}
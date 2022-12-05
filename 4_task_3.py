#  4_task_3
#  3. *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

keys = {i: {'name': input("name: "), 'email': input("email: ")} for i in range(2)}
empty_k = dict(keys)
print(empty_k)
# {0: {'name': 'ivan', 'email': 'inal@inal.by'}, 1: {'name': 'tom', 'email': 'tom@tom.by'}}

# name = input("name: ")    # поставь объявление вложенного словаря в генератор внешнего словаря
# email = input("email: ")
# n = int(input("n: "))
# keys = (i for i in range(1, n + 1)) # ключи поместим в кортеж
# value = [(name, email)] # значение каждого ключа вводим с клавиатуры
# empty_k = dict.fromkeys(keys, value) # создаём словарь
# print(empty_k)
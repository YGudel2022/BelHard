name = input("name: ")
email = input("email: ")
keys = (i: {(name, email)} for i in range(2)) # ключи поместим в кортеж
value = {(name, email)} # значение каждого ключа вводим с клавиатуры
empty_k = dict(keys)
print(empty_k)
# empty_k = dict.fromkeys(keys, value) # создаём словарь
# print(keys)

# keys = {i: {'name': input("name: "), 'email': input("email: ")} for i in range(2)}
# empty_k = dict(keys)
# print(empty_k)
# {0: {'name': 'ivan', 'email': 'inal@inal.by'}, 1: {'name': 'tom', 'email': 'tom@tom.by'}}


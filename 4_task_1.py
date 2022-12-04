# 4_task_1
# 1. Заполнить список степенями числа 2 (от 2^1 до 2^n).

nambers = int(input("Список от 2^1 до 2^n, где n =  "))
nambers_tuple = {2**i for i in range(1, nambers + 1)}         # кортеж из от 2^1 до 2^n
list_nambers_tuple = list(nambers_tuple)                      # преобразовали в список
list_nambers_tuple.sort()                                     # сортировка
print(list_nambers_tuple)

# Вариант 2
# как работает этот генератор?
# как результат стал строкой?
print(*[2 ** i for i in range(1, int(input("Число: ")) + 1)])
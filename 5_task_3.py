# Задача 3 **Вывести четные числа от 2 до N по 5 в строку

n = int(input("Введите n: "))
for i in range(2, n+1):
    if i%2 == 0:
        print(i)
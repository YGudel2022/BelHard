# 6_task_6 6. Дан список рандомных чисел, необходимо
# отсортировать его в виде, сначала четные, потом нечётные

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
print("Отфильтрованный список: ", list(out_filter))
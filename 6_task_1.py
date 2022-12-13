#1. 6_task_1 Написать функцию перевода десятичного числа
# в двоичное и обратно, без использования функции int

def decimal_to_binary(n):
    return bin(n).replace("0b", "")
if __name__ == '__main__':
    print(decimal_to_binary(2))
    print(decimal_to_binary(22))
    print(decimal_to_binary(222))

def binary_to_decimal(binary):
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)
if __name__ == '__main__':
    binary_to_decimal(10)
    binary_to_decimal(10110)
    binary_to_decimal(11011110)
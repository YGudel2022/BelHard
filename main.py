# x = float(input('Введите сумму вклада: '))
# p = float(input('Введите процент: '))
# y = float(input('Введите сумму: '))
# i = 0
# while x < y:
#     x *= 1 + p / 100
#     i += 1
# print('Понадобится ', i)


second = int(7336)
x = second // 3600
y = second // 60 - x*60
z = second % 60

print(x, y, z)

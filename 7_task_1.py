def PrintPasTriangle(rows):
  row = [1]
  for i in range(rows):
    print(row)
    row = [sum(x) for x in zip([0] + row, row + [0])]
PrintPasTriangle(13)

# # input n
# n = int(input("Enter the number of rows:"))
#
# # iterarte upto n
# for i in range(n):
#     # adjust space
#     print(' ' * (n - i), end='')
#
#     # compute power of 11
#     print(' '.join(map(str, str(11 ** i))))
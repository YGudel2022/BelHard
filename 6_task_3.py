# 3. 6_task_3 Дан список чисел и на вход поступает число N,
# необходимо сместить список на указанное число,
# пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
nums = [1, 2, 3, 4, 5, 6, 7]
print(nums)
shift(nums, 3)
print(nums)
shift(nums, 4)
print(nums)
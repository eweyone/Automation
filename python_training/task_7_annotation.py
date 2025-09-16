# a: int = 5
# b: str = 'строка'
# c: list = [1, 2]
#
# def indent(s: str, width: int) -> str:
#     return ' ' * (max(0, width - len(s))) + s
#
# print(indent('123', 123))

# # Задача 1
# def task_1(s: str = '') -> int:
#     return len(s)
#
# print(task_1())
#
# print(task_1('123456'))


# # Задача 2
# def task_2(a: list, b: list) -> int:
#     return max(len(a), len(b))
#
# print(task_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15]))

# #Задача 3
# def task_3(a:list):
#     return a + [3, 2, 1]
#
# print(task_3([1, 2, 3]))

# Задача 4
def task_4(a:list) -> int:
    return sum(a)

print(task_4([1, 2, 3, 4]))

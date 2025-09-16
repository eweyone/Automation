# Задача 1
def task_1() -> None:
    q:int = 1
    w:float = 1.5
    e:str = '2'
    r:list = [3, 4]
    t:bool = True
    print(type(q), type(w), type(e), type(r), type(t))
task_1()

# Задача 2
def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]) -> int:
    return a[0:3]

print(task_2(), 'Начало последовательности чисел Фибоначчи, '
                'где каждое последующее число является суммой двух предыдущих.')
#Последовательность заметил, название загуглил


# Задача 3
def task_3(b:int | float) -> int | float:
    return b ** 2

print(task_3(6))

print(task_3(2.5))
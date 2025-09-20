# Задача: Создать класс Input, принимающий 1 аргумент при инициализации (loc)
# Создать объект search(экземпляр класса Input)
# Вывести в консоль значение аргумента loc, объекта search
# class Input:
#
#     def __init__(self, loc):
#         self.loc = loc
#
# search = Input('input#search')
#
# print(search.loc)


# Задача 1*: Добавить к классу Input атрибут объекта text
# Создать классы: Button, Title, Link, для каждого прописать атрибуты text и loc
# Создать каждому классу объекты с любыми данными
# Вывести в консоль text и loc каждого класса



# Доп. Задание 5.
# папка python_training
# Создайте файл task_9_checks.py
# a. создайте класс Checks, принимающий 1 аргумент при инициализации (loc)
# b. создайте для него метод check_text, метод возвращает self.loc
# в файле task_9_oop_1.py
# c. наследуйте все классы от класса Checks
# i. чтобы использовать класс из другого файла его нужно импортировать
# from название файла(без расширения) import название класса
# d. переделайте все 4 класса в файле task_9_oop_1.py так чтоб в объектах можно было использовать методы родительского класса
# e. распечатайте в консоль результаты метода .check_text() вызванного от каждого объекта классов файла task_9_oop_1.py


from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search_one = Input('input#search', 'Локатор для класса Input')

print(search_one.loc)
print(search_one.text)
print(search_one.check_text())
print('\n')



class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search_two = Button('Button#search_two', 'Локатор для класса Button')

print(search_two.loc)
print(search_two.text)
print(search_two.check_text())
print('\n')



class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search_three = Title('Title#search_three', 'Локатор для класса Title')

print(search_three.loc)
print(search_three.text)
print(search_three.check_text())
print('\n')



class Link(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search_four = Link('Link#search_four', 'Локатор для класса Link')

print(search_four.loc)
print(search_four.text)
print(search_four.check_text())
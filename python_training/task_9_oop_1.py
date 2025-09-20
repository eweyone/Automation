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
class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_one = Input('input#search', 'Локатор для класса Input')

print(search_one.loc)
print(search_one.text)
print('\n')



class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_two = Button('Button#search_two', 'Локатор для класса Button')

print(search_two.loc)
print(search_two.text)
print('\n')



class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_three = Title('Title#search_three', 'Локатор для класса Title')

print(search_three.loc)
print(search_three.text)
print('\n')



class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_four = Link('Link#search_four', 'Локатор для класса Link')

print(search_four.loc)
print(search_four.text)
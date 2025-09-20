# Задача 2: Создать класс Page, принимающий 1 аргумент при инициализации url
# В этом классе реализовать метод get(), который выводит на печать url
# Создать объект home и вызвать метод get()
class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)

home = Page('/images/logo.png')


home.get()
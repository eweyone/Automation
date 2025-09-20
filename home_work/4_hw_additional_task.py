# Доп. Задача 4.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
            print('Автомобиль заведен')

    def stop_engine(self):
            print('Автомобиль заглушен')

    def set_year(self, set_year_value):
        if set_year_value:
            self.year = set_year_value
            print(self.year)
        else:
            print(self.year)

    def set_type(self, set_type_value):
        if set_type_value:
            self.type = set_type_value
            print(self.type)
        else:
            print(self.type)

    def set_color(self, set_color_value):
        if set_color_value:
            self.color = set_color_value
            print(self.color)
            print('\n')
        else:
            print(self.color)
            print('\n')


first_car = Car('Черный', 'Легковой автомобиль', '2016')
second_car = Car('Белый', 'Универсал', '2020')
third_car = Car('Красный', 'Внедорожник', '2025')

first_car.start_engine()
first_car.stop_engine()
first_car.set_year('2015')
first_car.set_type('Универсал')
first_car.set_color('Розовый')

second_car.start_engine()
second_car.stop_engine()
second_car.set_year('2019')
second_car.set_type('Грузовик')
second_car.set_color('Мокрый асфальт')

third_car.start_engine()
third_car.stop_engine()
third_car.set_year('2007')
third_car.set_type('Легковой автомобиль')
third_car.set_color('Морская волна')
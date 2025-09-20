# Задача 1.
# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

    def perimeter(self):
        print(2 * (self.width + self.height))
        print('\n')

case_one = Rectangle(5, 5)
case_two = Rectangle(10, 2)
case_three = Rectangle(3, 6)

case_one.area()
case_one.perimeter()

case_two.area()
case_two.perimeter()

case_three.area()
case_three.perimeter()



# Задача 2.
# Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        if self.b > 0:
            print(self.a / self.b)
            print('\n')
        else:
            print('На ноль делить нельзя!')
            print('\n')

    def subtraction(self):
        print(self.a - self.b)

example_one = Math(10, 5)
example_two = Math(-10, 2)
example_three = Math(25, 0)

example_one.addition()
example_one.subtraction()
example_one.multiplication()
example_one.division()

example_two.addition()
example_two.subtraction()
example_two.multiplication()
example_two.division()

example_three.addition()
example_three.subtraction()
example_three.multiplication()
example_three.division()



# Задача 3.
# откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:

    def __init__(self, text, type, loc=None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text}')

text_box = Button('Text Box', 'Кнопка', 'elements#text_box')
check_box = Button('Check Box', 'Кнопка', 'elements#check_box')
radio_button = Button('Radio Button', 'Кнопка')
web_tables = Button('Web Tables', 'Кнопка')
buttons = Button('Buttons', 'Кнопка')
broken_links_images = Button('Broken Links - Images', 'Кнопка')
upload_and_download = Button('Upload and Download', 'Кнопка')
dynamic_properties = Button('Dynamic Properties', 'Кнопка')

text_box.click()
check_box.click()
radio_button.click()
web_tables.click()
buttons.click()
broken_links_images.click()
upload_and_download.click()
dynamic_properties.click()
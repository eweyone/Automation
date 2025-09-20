from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/')

# Поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


# Делать в DevTools
# Задача 1 https://demoqa.com/
# Составить локатор для элемента <img src="/images/Toolsqa.jpg">
# > header > a > img

# Задача 2 Для подвала самый короткий локатор
# footer > span

# Задача 3 Поиск общего локатора для 6 кнопок
# [class="category-cards"]
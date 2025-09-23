# Задача 1.
# Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

def check_elements():
    username = driver.find_element(By.CSS_SELECTOR, '[id="user-name"]')
    password = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
    submit_button = driver.find_element(By.CSS_SELECTOR, '[id="login-button"]') # Кнопка называется не Submit, а Login

    if username and password and submit_button:
        print('Элементы найдены')
    else:
        print('Элементы не найдены')

    driver.quit()

check_elements()
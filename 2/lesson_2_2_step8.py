from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'test.txt')
print(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR, 'input.form-control[name="firstname"]')
    input1.send_keys("Iryna")
    input2 = browser.find_element(
        By.CSS_SELECTOR, 'input.form-control[name="lastname"]')
    input2.send_keys("Agapova")
    input3 = browser.find_element(
        By.CSS_SELECTOR, 'input.form-control[name="email"]')
    input3.send_keys("test@mail.ru")

    file_attach = browser.find_element(
        By.CSS_SELECTOR, 'input[type="file"]')
    file_attach.send_keys(file_path)

    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

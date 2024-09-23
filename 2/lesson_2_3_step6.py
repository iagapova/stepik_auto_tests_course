from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin, log


def calc(x):
    return log(abs(12*sin(x)))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # жмакаем кнопку и переходим на другую вкладку
    input1 = browser.find_element(
        By.CSS_SELECTOR, 'button.trollface')
    input1.click()

    # получаем следующую вкладку
    new_window = browser.window_handles[1]

    # переходим в другую вкладку
    browser.switch_to.window(new_window)

    num_res = browser.find_element(
        By.CSS_SELECTOR, 'label span:nth-child(2)')
    x = num_res.text
    res = calc(int(x))
    input2 = browser.find_element(
        By.CSS_SELECTOR, '#answer')
    input2.send_keys(res)

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

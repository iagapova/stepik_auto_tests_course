from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin, log


def calc(x):
    result = log(abs(12*sin(x)))
    return result


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_res = browser.find_element(
        By.CSS_SELECTOR, "label span:nth-child(2)")
    x = int(x_res.text)

    print("valuex of x: ", x)
    res = calc(x)
    print(res)

    answer = browser.find_element(
        By.ID, "answer")
    answer.send_keys(res)  # вводим результат
    time.sleep(1)

    input2 = browser.find_element(
        By.CSS_SELECTOR, "input#robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()

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

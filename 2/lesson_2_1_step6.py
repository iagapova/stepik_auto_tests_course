from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img_res = browser.find_element(By.CSS_SELECTOR, "img#treasure")

    img_valuex = img_res.get_attribute("valuex")
    print("valuex of img: ", img_valuex)

    # assert img_valuex is not None, "no value"

    y = calc(img_valuex)
    time.sleep(1)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    input2 = browser.find_element(
        By.CSS_SELECTOR, "input#robotCheckbox.check-input")
    input2.click()

    input3 = browser.find_element(
        By.CSS_SELECTOR, 'input#robotsRule.check-input')
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

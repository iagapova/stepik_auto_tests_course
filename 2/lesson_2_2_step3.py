from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_res = browser.find_element(
        By.CSS_SELECTOR, "h2 span:nth-child(2)#num1")
    num1 = num1_res.text
    print("valuex of num1: ", num1)
    num2_res = browser.find_element(
        By.CSS_SELECTOR, "h2 span:nth-child(4)#num2")
    num2 = num2_res.text
    print("valuex of num2: ", num2)
    # assert img_valuex is not None, "no value"

    time.sleep(1)
    my_sum = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(my_sum)

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

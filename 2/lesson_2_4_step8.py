from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from math import sin, log


def calc(x):
    return log(abs(12*sin(x)))


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), '$100'))

    button1 = browser.find_element(By.CSS_SELECTOR, "button#book")
    button1.click()

    num_res = browser.find_element(
        By.CSS_SELECTOR, 'label span:nth-child(2)')
    x = num_res.text
    res = calc(int(x))
    input2 = browser.find_element(
        By.CSS_SELECTOR, '#answer')
    input2.send_keys(res)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

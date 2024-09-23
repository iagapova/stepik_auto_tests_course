import time
from selenium import webdriver
# - класс, который содержит все возможные локаторы
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element(By.ID, "submit_button")

    print(button)

    # кликаем кнопку
    button.click()
    time.sleep(5)
finally:
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    browser.quit()

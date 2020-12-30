from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Xxx.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    browser.find_element_by_name("firstname").send_keys("Xxx")
    browser.find_element_by_name("lastname").send_keys("Xxx")
    browser.find_element_by_name("email").send_keys("Xxx")
    browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

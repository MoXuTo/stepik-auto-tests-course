from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x_element):
  return str(math.log(abs(12*math.sin(x_element))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value").text
    x = calc(int(x_element))

    browser.find_element_by_id("answer").send_keys(x)

    browser.find_element_by_id("robotCheckbox").click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element_by_id("robotsRule").click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

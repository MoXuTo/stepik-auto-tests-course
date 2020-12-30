from selenium import webdriver
import time
import math

def calc(x_element):
  return str(math.log(abs(12*math.sin(x_element))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value").text
    x = calc(int(x_element))
    browser.find_element_by_id("answer").send_keys(x)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()

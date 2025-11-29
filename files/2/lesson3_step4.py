from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    res = calc(x)

    placeholder = browser.find_element(By.ID, 'answer')
    placeholder.send_keys(res)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
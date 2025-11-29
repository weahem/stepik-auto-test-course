from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num1 = num1_element.text

    num2_element = browser.find_element(By.ID, "num2")
    num2 = num2_element.text

    res = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(res))
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
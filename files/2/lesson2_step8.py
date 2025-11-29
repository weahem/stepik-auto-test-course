from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name_input = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name_input.send_keys('Uga')

    lastname_input = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname_input.send_keys('Buga')

    email_input = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email_input.send_keys('ugabuga@email.me')

    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
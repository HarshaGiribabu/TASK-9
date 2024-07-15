from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")
time.sleep(3)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")
time.sleep(3)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(2)

page_title = driver.title
print(f"webpage title: {page_title}")

current_url = driver.current_url
print(f"Current URL of the webpage: {current_url}")

page_source = driver.page_source
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)

driver.quit()


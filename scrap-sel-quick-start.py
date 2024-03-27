from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Your login credentials
password = "Password123"
username = "student"

driver.get("https://practicetestautomation.com/practice-test-login/")

#find the username input field and enter the specified username
username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys(username)

#find the password input field and enter the specified password
password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(password)

#find the form's submit button and click it
submit_button = driver.find_element(by=By.ID, value="submit")
submit_button.click()

#wait for the new page to load
time.sleep(3)

#verify new page URL
print(driver.current_url)
assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url, "URL check failed"

# Verify page contains expected text
page_text = driver.find_element(by=By.TAG_NAME, value="body").text
assert "Congratulations" in page_text or "Logged In Successfully" in page_text, "Text check failed"

# Verify Log out button is displayed
logout_button = driver.find_element(by=By.XPATH, value="//a[contains(text(), 'Log out')]")
assert logout_button.is_displayed(), "Log out button not displayed"

print("Test case passed according to https://practicetestautomation.com/practice-test-login/ specifications")
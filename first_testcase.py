import time

"""
home page:
https://magento.softwaretestingboard.com/

login page:
https://magento.softwaretestingboard.com/customer/account/login/
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = 'https://magento.softwaretestingboard.com/customer/account/login/'
expected_title = "Customer Login Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites"

textbox_email_xpath = "//input[@name='login[username]']"
textbox_password_xpath = "//input[@name='login[password]']"
button_sign_in_xpath = "//button[@class='action login primary']"

str_email = "roni_cost@example.com"
str_password = "roni_cost3@example.com"

service = Service(executable_path='../../drivers/chromedriver')
driver = webdriver.Chrome(service=service)

try:
    driver.get(url=URL)
    actual_title = driver.title

    # check the title
    if actual_title == expected_title:
        print('titles match')
    else:
        print(f'Actual title {actual_title} is not equal to expected {expected_title}')

    email_textbox = driver.find_element(By.XPATH, textbox_email_xpath)
    email_textbox.send_keys(str_email)

    password_textbox = driver.find_element(By.XPATH, textbox_password_xpath)
    password_textbox.send_keys(str_password)

    time.sleep(5)

    sign_in_button = driver.find_element(By.XPATH, button_sign_in_xpath)
    sign_in_button.click()

    time.sleep(5)
finally:
    driver.quit()

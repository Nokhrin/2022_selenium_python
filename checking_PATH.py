import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://demoqa.com/')

time.sleep(5)

print(driver.current_url)
print(driver.title)
print(driver.get_window_size)

driver.quit()

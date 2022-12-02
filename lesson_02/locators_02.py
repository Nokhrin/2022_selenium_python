# TODO: css selectors for https://demo.realworld.io/

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service


# service = Service()
# driver = webdriver.Chrome(service)
driver = webdriver.Chrome()

try:
    driver.get('https://www.saucedemo.com/')
    print(driver.title)

    driver.maximize_window()

    textbox_username_xpath = "//input[@id='user-name']"
    textbox_password_xpath = "//input[@id='password']"
    input_login_button_xpath = "//input[@id='login-button']"

    """
    Accepted usernames are:
    standard_user
    locked_out_user
    problem_user
    performance_glitch_user

    Password for all users:
    secret_sauce
    """
    username = 'standard_user'
    password = 'secret_sauce'

    driver.find_element(by=By.XPATH, value=textbox_username_xpath).send_keys(username)
    driver.find_element(by=By.XPATH, value=textbox_password_xpath).send_keys(password)
    driver.find_element(by=By.XPATH, value=input_login_button_xpath).click()

    product_linktext = "Sauce Labs Bike Light"
    product = driver.find_element(by=By.LINK_TEXT, value=product_linktext)

    # get all attributes of WebElement using Javascript
    # https://stackoverflow.com/a/56383984/9232392
    attrs = []
    for attr in product.get_property('attributes'):
        attrs.append(str([attr['name'], attr['value']]))
    # print('\n'.join(attrs))

    print(product.get_attribute('href'))
    print(product.get_attribute('id'))

    # get multiple web elements
    img_items_xpath = "//img[@class='inventory_item_img']"
    items_imgs = driver.find_elements(by=By.XPATH, value=img_items_xpath)
    print(f'items_imgs count:{len(items_imgs)}')
    print(f'items_imgs: {items_imgs}')

    div_prices_xpath = "//div[@class='inventory_item_price']"
    items_prices = driver.find_elements(by=By.XPATH, value=div_prices_xpath)
    print(f'prices count: {len(items_prices)}')
    print(f'prices: {items_prices}')

finally:
    driver.quit()

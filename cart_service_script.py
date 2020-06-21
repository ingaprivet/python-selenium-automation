from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(
    executable_path='/Users/ingabukhvalova/PycharmProjects/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

cart_icon = driver.find_element(By.ID, 'nav-cart')
cart_icon.click()

text_expected = driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")

driver.quit()

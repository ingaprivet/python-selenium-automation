from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(
    executable_path='/Users/ingabukhvalova/PycharmProjects/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
driver.implicitly_wait(4)

# declare 2 variables
bestsellers_text = (By.CSS_SELECTOR, "div#zg_banner_text")
bestsellers_links = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']")


driver.quit()

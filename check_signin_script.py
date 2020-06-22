import selenium
from selenium.webdriver.common.by import By

# init driver
driver = selenium.webdriver.Chrome(
    executable_path='/Users/ingabukhvalova/PycharmProjects/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

input_field = driver.find_element(By.ID, 'nav-orders')

search_icon = driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")

search_icon.click()


driver.quit()

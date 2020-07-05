from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException, TimeoutException

# initialize the driver
driver = webdriver.Chrome(
    executable_path='/Users/ingabukhvalova/PycharmProjects/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

# click on link
link_found = driver.find_element(By.XPATH, "//*[text()[contains(.,'See daily updates at blog.aboutamazon.com')]]")
link_found.click()

# windows handling
handles = driver.window_handles
size = len(handles)
parent_handle = driver.current_window_handle
for x in range(size):
    if handles[x] != parent_handle:
        driver.switch_to.window(handles[x])
        print(f'child window page title: ' + driver.title)
        driver.close()
        break

driver.switch_to.window(parent_handle)

driver.quit()

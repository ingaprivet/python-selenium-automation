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
driver.get('https://www.amazon.com/s?k=echo+dot&ref=nb_sb_noss_2')
driver.implicitly_wait(4)



#click on element
element_found = driver.find_element(By.XPATH, "//img[@alt='Echo Dot (3rd Gen) - Smart speaker with clock and Alexa - Sandstone']")
print ("found element = {0}".format(element_found))
element_found.click()

#wait
wait=WebDriverWait(driver, 10)
something=wait.until(EC.presence_of_element_located((By.XPATH, '//meta[@content="echo dot"]')))

#add to cart
driver.find_element_by_xpath('//input[@id="add-to-cart-button"]').click()




try:
    WebDriverWait(driver, 3).until(EC.new_window_is_opened,
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
    alert = driver.switch_to.window()
    alert.dismiss()
    print("alert accepted")
except TimeoutException:
    print("no alert")


#verify and quit
text_expected = driver.find_element(By.XPATH, "//span[contains(text(),'(1 item):')]")

driver.quit()


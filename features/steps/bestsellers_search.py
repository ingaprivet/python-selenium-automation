from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait

TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')


@given('Open amazon BestSellers page')
def open_amazon_bestsellers(context):
    # context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bsms_tab')
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify each top link opens a new page')
def click_open_new_page(context):
    # list_of_links = context.driver.find_element_by_xpath("//div[@id='zg_tabs']") #WebElement
    # list_of_links = context.driver.find_elements_by_css_selector("a[href*='zg_bs_tab']")  # list object
    list_of_links = WebDriverWait(context.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                                                   "a["
                                                                                                   "href*='zg_bs_tab']")))  # Induce WebDriverWait for the visibility of the desired elements
    windows_before = context.driver.current_window_handle  # Store the parent_window_handle for future use
    array_of_links = []
    array_of_text = []
    index = 0

    for link in list_of_links:
        link_info = link.get_attribute("href")
        array_of_links.append(link_info)
        text_info = link.get_attribute("text")
        array_of_text.append(text_info)

    for link in list_of_links:
        url_link = array_of_links[index]  # url from the saved array
        text_info_default = array_of_text[index]


        # context.driver.execute_script("window.open(arguments[0])", url_link)  # Open the hrefs one by one through execute_script method in a new tab
        context.driver.execute_script(
            "window.open('" + url_link + "');")  # Open the hrefs one by one through execute_script method in a new tab
        WebDriverWait(context.driver, 10).until(
            EC.number_of_windows_to_be(2))  # Induce  WebDriverWait for the number_of_windows_to_be 2

        assert url_link == array_of_links[
            index], f'Expected {array_of_links[index]} url address, but got {url_link} url address'

        windows_after = context.driver.window_handles

        #new_window = [x for x in windows_after if x != windows_before][0] # Identify the newly opened window

        for x in windows_after:
            if x != windows_before[0]:
                context.driver.switch_to.window(x)  # switch_to the new window

        # perform your webscrapping here
        print("Perform your verification on page {}".format(context.driver.title))
        context.driver.wait.until(EC.presence_of_element_located((By.ID, 'zg_banner_text_wrapper')))
        text_info_current = context.driver.find_element_by_id('zg_banner_text_wrapper').text

        context.driver.close()  # close the window
        context.driver.switch_to.window(windows_before)  # switch_to the parent_window_handle
        #context.driver.switch_to.default_content()

        index += 1
        assert text_info_default in text_info_current, f'Expected {text_info_default} to be in {text_info_current}'

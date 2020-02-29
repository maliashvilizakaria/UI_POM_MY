# Test Case
# 1. Open browser chrome browser
# 2. Launch the 'automationpractice.com'
# 3. Enter 't-shirt' in search box
# 4. Click search button (option2: hit ENTER key on keyboard)
# 5. Verify at least one product displayed/appeared

from selenium import webdriver
import time

# CONSTANTS
# chrome_url = "C:\\dev\\chromedriver_win32\\chromedriver.exe"
home_url = "http://automationpractice.com"
keyword = 't-shirt'


def test_launching_site(browser):
    browser.get(home_url)


def test_entering_the_keyword(browser):
    searchbox = browser.find_element_by_name("search_query")
    # searchbox.send_keys('iphone')
    # searchbox.submit()
    # time.sleep(10)
    searchbox.clear()
    time.sleep(3)
    searchbox.send_keys(keyword)
    time.sleep(5)
    # browser.find_element_by_name("submit_search").click()
    searchbox.submit()
    print("submitting the form")


def test_verify_result(browser):
    products_list = browser.find_elements_by_xpath(
        "//*[@id='center_column']/ul/li")
    assert len(products_list) >= 1
    time.sleep(5)

# HW: google search
# resulttext = browser.find_element_by_xpath("//*[@id='mBMHK']").text
# try to send keys 'iphone', clear and send key 'python'
    # "About 494,000,000 results (0.56 seconds) "
    # get the number parse it to numbers only then convert to int, apply the condition :
    # 1. split(), split(","), ''.join(numlist), int(strnumber)
    #   if 494000000 > 300000000 :
    #     assert True
    # else:
    #     assert False

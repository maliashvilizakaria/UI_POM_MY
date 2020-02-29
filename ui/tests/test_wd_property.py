from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# CONSTANTS
# chrome_url = "C:\\dev\\chromedriver_win32\\chromedriver.exe"
home_url = "http://automationpractice.com"
keyword = 't-shirt'


def test_launching_site(browser):
    browser.get(home_url)


def test_wd_properties(browser):
    print("*******************************************")
    print(browser.title)
    print(browser.current_url)
    print(browser.name)
    handle = browser.current_window_handle
    # click button to open new window
    # handle2 = browser.current_window_handle
    print(handle)
    # browser.switch_to.window(handle)
    # browser.switch_to.window(handle2)
    # handles = browser.window_handles  # return the handles of all open windows on your browser
    # browser.switch_to.window(handles[0])  # swithc to first tab
    # browser.switch_to.window(handles[1])  # swithc to first tab

def test_wd_methods(browser):
    # auto format the code >> SHIFT+ALT+F
    print(f"Current url: {browser.current_url}")
    wmenu = browser.find_element_by_xpath(
        "//a[@class='sf-with-ul'][contains(text(),'Women')]")

    wmenu.click()
    print(f"URL after clicing the menu: {browser.current_url}")
    browser.back()
    print(f"url after Back button : {browser.current_url}")
    browser.forward()
    print(f"after clicking the forward button : {browser.current_url}")
    print("****************************************")
    
    # search_box = browser.find_element_by_xpath('search')
    # search_box.send_keys(Keys.ENTER)
    # search_box.submit()

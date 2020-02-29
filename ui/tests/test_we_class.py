from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


# search_box = browser.find_element_by_xpath('search')
# search_box.send_keys(Keys.ENTER)
# search_box.submit()

def test_forms_textboxes(browser):
    """working with forms, textboxes, checkboxes, and radio buttons."""
    url = "http://the-internet.herokuapp.com/login"

    browser.get(url)
    sleep(5)
    # element locators
    username = browser.find_element_by_xpath("//input[@id='username']")
    passwrod = browser.find_element_by_xpath("//input[@id='password']")
    login = browser.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']")

    username.send_keys("tomsmith")
    passwrod.send_keys("SuperSecretPassword!")
    login.click()
    sleep(10)

    # testing the message text area
    expected_message = "Welcome to the Secure Area. When you are done click logout below."
    message = browser.find_element_by_xpath("//h4[@class='subheader']").text
    assert expected_message == message.strip(), "Assert failed!!!"

    # verify logout button displayed, if displayed click logout
    logout = browser.find_element_by_xpath("//i[@class='icon-2x icon-signout']")
    if logout.is_displayed():
        logout.click()
    else:
        print("logout is not displayed")

    # check the login page is opened
    assert url in browser.current_url, "This is the message if url assert fails"


def test_checkbox(browser):
    url = "http://the-internet.herokuapp.com/checkboxes"

    browser.get(url)
    sleep(5)
    element1 = browser.find_element_by_xpath("//body//input[1]")
    element2 = browser.find_element_by_xpath("//body//input[2]")

    # logic for element1
    if element1.is_selected():
        element1.click()
        print("unselecting the element1")
    else:
        element1.click()
        print("selecting the element1")

    # logic for element2
    if element2.is_selected():
        element2.click()
        print("unselecting the element2")
    else:
        element2.click()
        print("selecting the element2")

    sleep(15)

@pytest.mark.dropdowntest
def test_dropdown(browser):
    url = "http://the-internet.herokuapp.com/dropdown"

    browser.get(url)
    sleep(5)
    dropdown_element = browser.find_element_by_xpath("//select[@id='dropdown']")
    dropdown_list = Select(dropdown_element)
    ddown_values = [value.text.strip() for value in browser.find_elements_by_xpath('//select/option')]
    # ddown_values.sort()
    print(ddown_values)
    sorted_ddown_values = sorted(ddown_values)
    print(sorted_ddown_values)

    # assert ddown_values == sorted_ddown_values 
    for sorted_value in sorted_ddown_values:
         dropdown_list.select_by_visible_text(sorted_value)
         sleep(5)

    print(dropdown_list.first_selected_option.text)
    assert dropdown_list.first_selected_option.text.strip() == "Please select an option"
    sleep(5)
    dropdown_list.select_by_visible_text("Option 2")
    sleep(5)
    # dropdown_list.deselect_by_visible_text("Option 2")
    dropdown_list.select_by_value("1")
    sleep(5)
    dropdown_list.select_by_index(2)  # should select Option 2
    sleep(3)
    assert len(dropdown_list.options) == 3, "List of Options Check Failed"


def test_alerts(browser):
    url = "http://the-internet.herokuapp.com/javascript_alerts"
    text_to_enter = "Hello Selenium!"

    browser.get(url)
    sleep(5)
    js_prompt_button = browser.find_element_by_xpath(
        "//button[contains(text(),'Click for JS Prompt')]")
    js_prompt_button.click()

    alert = browser.switch_to.alert

    alert_msg = alert.text
    print(f"message displayed : {alert_msg}")
    alert.send_keys(text_to_enter)
    sleep(10)
    alert.accept()

    sleep(5)
    result = browser.find_element_by_xpath("//p[@id='result']").text
    # You entered: 456
    assert result.split(":")[1].strip() == text_to_enter

    # cancel the alert
    js_prompt_button = browser.find_element_by_xpath(
        "//button[contains(text(),'Click for JS Prompt')]")
    js_prompt_button.click()

    alert = browser.switch_to.alert
    alert.dismiss()


def test_explicit_wait(browser):
    url = "http://the-internet.herokuapp.com/checkboxes"
    wait = WebDriverWait(browser, 20)

    browser.get(url)
    sleep(5)
    # element1 = browser.find_element_by_xpath("//body//input[1]")
    # element2 = browser.find_element_by_xpath("//body//input[2]")
    element1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//body//input[1]")))
    element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//body//input[2]")))

    # logic for element1
    if element1.is_selected():
        element1.click()
        print("unselecting the element1")
    else:
        element1.click()
        print("selecting the element1")

    # logic for element2
    if element2.is_selected():
        element2.click()
        print("unselecting the element2")
    else:
        element2.click()
        print("selecting the element2")

    sleep(15)

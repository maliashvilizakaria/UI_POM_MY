from features.ui.all_imports import *

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, element):
        element.click()


class Login(BasePage):::

    # LOCATORS
    username_box = "//input[@id='username']"
    password_box = "//input[@id='password']"
    login_button =  "//i[@class='fa fa-2x fa-sign-in']"

    # ACTIONS ON THE PAGE
    def enter_username(self, uname):
        username = self.driver.find_element_by_xpath(self.username_box)
        username.clear()
        username.send_keys(uname)

    def enter_password(self, phrase):
        password = self.driver.find_element_by_xpath(self.password_box)
        password.clear()
        password.send_keys(phrase)

    def click_login(self):
        self.driver.find_element_by_xpath(self.ogin_button).click()

    @property
    def get_title(self):
        return self.driver.title

class PopUpWindow(BasePage):

    openwindow_button = "//button[@id='openwindow']"
    search_box = "//input[@id='search-courses']"


    def click_openwindow(self):
        element = self.driver.find_element_by_xpath(self.openwindow_button)
        element.click()

    def search_text(self, text):
        element = self.driver.find_element_by_xpath(self.search_box)
        element.clear()
        element.send_keys(text)
        element.submit()

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    # step: 1  - SETUP (before your scope)
    # driver = webdriver.Chrome(chrome_url)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    # TEARDOWN (after your scope)
    # step: 6 - closing the browser
    driver.quit()

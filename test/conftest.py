import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://booking.kai.id")

    yield driver
    driver.close()




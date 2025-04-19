import time

from selenium import webdriver
import allure
import pytest



@allure.title("Open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https://app.com")
    time.sleep(15)
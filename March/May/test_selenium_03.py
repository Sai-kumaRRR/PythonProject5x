import allure
import pytest
from selenium import webdriver

def test_vwo_sample_selenium_3():
    driver_path = '/Users/sai/Downloads/edge/msedgedriver'
    driver = webdriver.EdgeService(executable_path=driver_path)
    driver.get("https://app.vwo.com")



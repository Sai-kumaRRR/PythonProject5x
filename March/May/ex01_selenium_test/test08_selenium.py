import allure
import pytest
from selenium import webdriver
import time



def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(20)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    # driver.close() # current window
    driver.quit()
 # close everything.
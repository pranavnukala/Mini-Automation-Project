from selenium import webdriver
import time
import pytest
from pages.Login_page import Login
@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(90)
    driver.get("https://qamoviesapp.ccbp.tech")
    yield driver
    time.sleep(1)
    driver.close()

@pytest.fixture
def logged_in_driver(setup):
    login = Login(setup)
    login.enter_username("rahul")  
    login.enter_password("rahul@2021")
    login.loginbtn_click()
    yield setup

     
    
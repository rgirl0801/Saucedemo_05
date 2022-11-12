from selenium.webdriver.common.by import By


class LoginLocators:
    input_username = {'by': By.ID, 'v': 'user-name'}
    input_password = {'by': By.ID, 'v': 'password'}
    login_btn = {'by': By.ID, 'v': 'login-button'}
    hamburger_btn = {'by': By.ID, 'v': 'react-burger-menu-btn'}
    logout_btn = {'by': By.ID, 'v': 'logout_sidebar_link'}
    title = 'Swag Labs'

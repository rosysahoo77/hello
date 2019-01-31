from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
    def get_username_textbox(self):
        try:
            element = self.driver.find_element_by_name("user")
            return element
        except NoSuchElementException:
            return None
    def get_password_textbox(self):
        try:
            element = self.driver.find_element_by_name("pass")
            return element
        except NoSuchElementException:
            return None
    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@value='Log In']")
        except NoSuchElementException:
            return None
    def get_clear_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@value='Clear']")
        except NoSuchElementException:
            return None
    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_xpath("//input[@value='Log In']")))
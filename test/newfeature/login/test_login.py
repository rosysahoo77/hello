from lib.ui.login_page import LoginPage
from lib.utils import create_driver
import unittest
import json
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login = LoginPage(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_login(self):
        test_data = json.load(open('test/newfeature/login/login.JSON'))
        self.login.wait_for_login_page_to_load()

        self.login.get_username_textbox().send_keys(test_data['login']['username'])
        self.login.get_password_textbox().send_keys(test_data['login']['password'])

        self.login.get_login_button().click()

        expected_ele= self.driver.find_element_by_xpath("//a[text()='Help']")
        assert expected_ele.is_displayed() == True

from lib.ui.login_page import LoginPage
from lib.utils import create_driver
from lib.ui.sail_home_page import SailHomePage
import unittest
import json
class TestCreateParamFileValidP384(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login = LoginPage(self.driver)
        self.sail = SailHomePage(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_login(self):
        test_data = json.load(open('test/newfeature/login/login.JSON'))
        test_data1 = json.load(open('test/newfeature/create_cert_ECDSA/createcert.JSON'))
        self.login.wait_for_login_page_to_load()

        self.login.get_username_textbox().send_keys(test_data['login']['username'])
        self.login.get_password_textbox().send_keys(test_data['login']['password'])

        self.login.get_login_button().click()
        self.sail.get_configuration_link().click()
        self.sail.get_network_link().click()
        self.sail.get_ssltls_cert_manager_link().click()
        self.sail.get_gen_ECDSA_params_link().click()
        self.sail.get_gen_ECDSA_params_file_textbox().clear()
        self.sail.get_gen_ECDSA_params_file_textbox().send_keys(test_data1['createcert']['ECDSA parameter filename'])
        if(self.sail.get_NTST_curve_P384_checkbox().is_selected()):
            self.sail.get_gen_ECDSA_params_button().click()
        else:
            self.sail.get_NTST_curve_P384_checkbox().click()
            self.sail.get_gen_ECDSA_params_button().click()
        try:
            self.sail.get_exist_par_file_continue_button().click()
        except:
            return None

        expected_ele= self.driver.find_element_by_xpath("//b[text()='ECDSA Parameters generated']")
        assert expected_ele.is_displayed() == True



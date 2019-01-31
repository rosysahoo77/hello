from lib.ui.login_page import LoginPage
from lib.utils import create_driver
from lib.ui.sail_home_page import SailHomePage
import unittest
import json

class TestCreateCertSHA384Valid(unittest.TestCase):
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
        self.sail.wait_for_cert_create_page_to_load()
        self.sail.get_ECDSA_generate_cert_link().click()
        self.sail.get_create_ECDSA_param_file_name_textbox().clear()
        self.sail.get_create_ECDSA_param_file_name_textbox().send_keys\
            (test_data1['createcert']['ECDSA parameter filename'])
        self.sail.get_create_ECDSA_cert_file_name_textbox().clear()
        self.sail.get_create_ECDSA_cert_file_name_textbox().send_keys\
            (test_data1['createcert']['ECDSA Certificate File Name'])
        self.sail.get_create_ECDSA_private_key_file_name_textbox().clear()
        self.sail.get_create_ECDSA_private_key_file_name_textbox().clear()
        self.sail.get_create_ECDSA_private_key_file_name_textbox().send_keys\
            (test_data1['createcert']['ECDSA Private Key File Name'])
        self.sail.get_create_ECDSA_pwd_textbox().send_keys(test_data1['createcert']['Password'])
        self.sail.get_create_ECDSA_confirm_pwd_textbox().\
            send_keys(test_data1['createcert']['Confirm Password'])
        self.sail.get_create_ECDSA_cert_validity_textbox().clear()
        self.sail.get_create_ECDSA_cert_validity_textbox().\
            send_keys(test_data1['createcert']['Certificate valid for'])
        self.sail.get_create_ECDSA_common_name_textbox().clear()
        self.sail.get_create_ECDSA_common_name_textbox().send_keys(test_data1['createcert']['Common Name'])
        self.sail.get_create_ECDSA_org_name_textbox().clear()
        self.sail.get_create_ECDSA_org_name_textbox().send_keys(test_data1['createcert']['Organization Name'])
        self.sail.get_create_ECDSA_org_unit_name_textbox().clear()
        self.sail.get_create_ECDSA_org_unit_name_textbox().\
            send_keys(test_data1['createcert']['Organization Unit Name'])
        self.sail.get_create_ECDSA_locality_textbox().clear()
        self.sail.get_create_ECDSA_locality_textbox().send_keys(test_data1['createcert']['Locality'])
        self.sail.get_create_ECDSA_state_textbox().clear()
        self.sail.get_create_ECDSA_state_textbox().send_keys(test_data1['createcert']['State'])
        self.sail.get_create_ECDSA_country_textbox().clear()
        self.sail.get_create_ECDSA_country_textbox().send_keys(test_data1['createcert']['Country'])
        self.sail.get_create_ECDSA_email_textbox().clear()
        self.sail.get_create_ECDSA_email_textbox().send_keys(test_data1['createcert']['E-mail'])

        self.sail.get_create_ECDSA_SHA384_radiobutton().click()
        self.sail.get_create_ECDSA_gen_cert_button().click()
        try:
            self.sail.get_create_ESDSA_cotinue_button().click()
        except:
            return None
        expected_ele = self.driver.find_element_by_xpath("//b[text()='Certificate and Key generated']")
        assert expected_ele.is_displayed() == True


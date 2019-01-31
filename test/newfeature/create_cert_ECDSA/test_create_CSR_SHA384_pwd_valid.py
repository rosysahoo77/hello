from lib.ui.login_page import LoginPage
from lib.utils import create_driver
from lib.ui.sail_home_page import SailHomePage
import unittest
import json

class TestCreateCSRSHA384pwdValid(unittest.TestCase):
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
        self.sail.get_create_ESDSA_CSR_link().click()
        self.sail.get_create_ESDSA_CSR_paramfile_textbox().clear()
        self.sail.get_create_ESDSA_CSR_paramfile_textbox().send_keys\
            (test_data1['createcert']['ECDSA parameter filename'])
        self.sail.get_create_ESDSA_CSR_certfile_textbox().clear()
        self.sail.get_create_ESDSA_CSR_certfile_textbox().send_keys\
            (test_data1['createcert']['ECDSA CSR File Name'])
        self.sail.get_create_ESDSA_CSR_keyfile_textbox().clear()
        self.sail.get_create_ESDSA_CSR_keyfile_textbox().send_keys\
            (test_data1['createcert']['ECDSA Private Key File Name'])
        self.sail.get_create_ESDSA_CSR_pwd_textbox().send_keys\
            (test_data1['createcert']['Password'])
        self.sail.get_create_ESDSA_CSR_conpwd_textbox().send_keys\
            (test_data1['createcert']['Confirm Password'])
        self.sail.get_create_ESDSA_CSR_comname_textbox().clear()
        self.sail.get_create_ESDSA_CSR_comname_textbox().send_keys\
            (test_data1['createcert']['Common Name'])
        self.sail.get_create_ESDSA_CSR_orgname_textbox().clear()
        self.sail.get_create_ESDSA_CSR_orgname_textbox().send_keys\
            (test_data1['createcert']['Organization Name'])
        self.sail.get_create_ESDSA_CSR_orgunitname_textbox().clear()
        self.sail.get_create_ESDSA_CSR_orgunitname_textbox().send_keys\
            (test_data1['createcert']['Organization Unit Name'])
        self.sail.get_create_ESDSA_CSR_loc_textbox().clear()
        self.sail.get_create_ESDSA_CSR_loc_textbox().send_keys\
            (test_data1['createcert']['Locality'])
        self.sail.get_create_ESDSA_CSR_state_textbox().clear()
        self.sail.get_create_ESDSA_CSR_state_textbox().send_keys\
            (test_data1['createcert']['State'])
        self.sail.get_create_ESDSA_CSR_country_textbox().clear()
        self.sail.get_create_ESDSA_CSR_country_textbox().send_keys\
            (test_data1['createcert']['Country'])
        self.sail.get_create_ESDSA_CSR_email_textbox().clear()
        self.sail.get_create_ESDSA_CSR_email_textbox().send_keys\
            (test_data1['createcert']['E-mail'])
        self.sail.get_create_ESDSA_CSR_SHA384_radiobutton().click()
        self.sail.get_create_ESDSA_CSR_genCSR_button().click()
        try:
            self.sail.get_create_ESDSA_CSR_continue_button().click()
        except:
            return None

        expected_ele = self.driver.find_element_by_xpath("//b[text()='Error, CSR and Key not generated']")
        assert expected_ele.is_displayed() == True




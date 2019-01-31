from lib.ui.login_page import LoginPage
from lib.utils import create_driver
from lib.ui.sail_home_page import SailHomePage
import unittest
import json
class TestCreateCertSHA1inValid(unittest.TestCase):
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
        # Enter username of SAIL
        self.login.get_username_textbox().send_keys(test_data['login']['username'])
        # Enter password of SAIL
        self.login.get_password_textbox().send_keys(test_data['login']['password'])
        # Click on login
        self.login.get_login_button().click()
        # Click on configuration link
        self.sail.get_configuration_link().click()
        # Click on network link
        self.sail.get_network_link().click()
        # Click on SSL/TLS certificate manager link
        self.sail.get_ssltls_cert_manager_link().click()
        # Wait for the create certificate page to load
        self.sail.wait_for_cert_create_page_to_load()
        # Click on ECDSA generate certificate link
        self.sail.get_ECDSA_generate_cert_link().click()
        # Clear existing ECDSA parameter filename
        self.sail.get_create_ECDSA_param_file_name_textbox().clear()
        # Enter filename for ECDSA parameter file
        self.sail.get_create_ECDSA_param_file_name_textbox().send_keys\
            (test_data1['createcert']['ECDSA parameter filename'])
        # Clear existing ECDSA certificate file name
        self.sail.get_create_ECDSA_cert_file_name_textbox().clear()
        # Enter ECDSA certificate file name
        self.sail.get_create_ECDSA_cert_file_name_textbox().send_keys\
            (test_data1['createcert']['ECDSA Certificate File Name'])
        # Clear existing private key file name
        self.sail.get_create_ECDSA_private_key_file_name_textbox().clear()
        # Enter ECDSA private key filename
        self.sail.get_create_ECDSA_private_key_file_name_textbox().send_keys\
            (test_data1['createcert']['ECDSA Private Key File Name'])
        # Enter password for the certificate file
        self.sail.get_create_ECDSA_pwd_textbox().send_keys(test_data1['createcert']['Password'])
        # Enter password again for the certificate file
        self.sail.get_create_ECDSA_confirm_pwd_textbox().\
            send_keys(test_data1['createcert']['Confirm Password'])
        # Clear existing certificate validity date
        self.sail.get_create_ECDSA_cert_validity_textbox().clear()
        # Enter certificate validity date
        self.sail.get_create_ECDSA_cert_validity_textbox().\
            send_keys(test_data1['createcert']['Certificate valid for'])
        # Clear existing common name
        self.sail.get_create_ECDSA_common_name_textbox().clear()
        # Enter common name for the certificate
        self.sail.get_create_ECDSA_common_name_textbox().send_keys(test_data1['createcert']['Common Name'])
        # Clear existing organization name
        self.sail.get_create_ECDSA_org_name_textbox().clear()
        # Enter organization name
        self.sail.get_create_ECDSA_org_name_textbox().send_keys(test_data1['createcert']['Organization Name'])
        # Clear organization unit name text box
        self.sail.get_create_ECDSA_org_unit_name_textbox().clear()
        # Enter Organization unit name
        self.sail.get_create_ECDSA_org_unit_name_textbox().\
            send_keys(test_data1['createcert']['Organization Unit Name'])
        # Clear existing locality text box
        self.sail.get_create_ECDSA_locality_textbox().clear()
        # Enter locality
        self.sail.get_create_ECDSA_locality_textbox().send_keys(test_data1['createcert']['Locality'])
        # Clear state text box
        self.sail.get_create_ECDSA_state_textbox().clear()
        # Enter state
        self.sail.get_create_ECDSA_state_textbox().send_keys(test_data1['createcert']['State'])
        # Clear country text box
        self.sail.get_create_ECDSA_country_textbox().clear()
        # Enter country name
        self.sail.get_create_ECDSA_country_textbox().send_keys(test_data1['createcert']['Country'])
        # Clear email text box
        self.sail.get_create_ECDSA_email_textbox().clear()
        # Enter email id
        self.sail.get_create_ECDSA_email_textbox().send_keys(test_data1['createcert']['E-mail'])
        # Select SHA1 radio button
        self.sail.get_create_ECDSA_SHA1_radiobutton().click()
        # click on generate certificate and key button
        self.sail.get_create_ECDSA_gen_cert_button().click()
        try:
            # Click on continue button if certificate already exists with the same name
            self.sail.get_create_ESDSA_cotinue_button().click()
        except:
            return None
        # Check for the error message
        expected_ele = self.driver.find_element_by_xpath("//b[text()='Error, Certificate and Key not generated']")

        assert expected_ele.is_displayed() == True


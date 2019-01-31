from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class SailHomePage():
    def __init__(self,driver):
        self.driver = driver
    def get_configuration_link(self):
        try:
            element = self.driver.find_element_by_link_text('Configuration')
            return element
        except NoSuchElementException:
            return None

    def get_network_link(self):
        try:
            element = self.driver.find_element_by_link_text('Network')
            return element
        except NoSuchElementException:
                return None

    def get_ssltls_cert_manager_link(self):
        try:
            element = self.driver.find_element_by_link_text('SSL/TLS Certificate Manager')
            return element
        except NoSuchElementException:
                return None


    def get_gen_ECDSA_params_link(self):
        try:
            element = self.driver.find_element_by_link_text('Generate ECDSA Parameters')
            return element
        except NoSuchElementException:
                return None

    def get_gen_ECDSA_params_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Generate ECDSA Parameters']")
            return element
        except NoSuchElementException:
                return None
    def get_gen_ECDSA_params_file_textbox(self):
        try:
            element = self.driver.find_element_by_name('ecdsaparamfile')
            return element
        except NoSuchElementException:
                return None
    def get_NTST_curve_P256_checkbox(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='prime256v1']")
            return element
        except NoSuchElementException:
                return None
    def get_NTST_curve_P384_checkbox(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='secp384r1']")
            return element
        except NoSuchElementException:
                return None
    def get_NTST_curve_P521_checkbox(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='secp521r1']")
            return element
        except NoSuchElementException:
                return None
    #COntinue button on ECDSA parameter page when a certificated with the same name already exists
    def get_exist_par_file_continue_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Continue']")
            return element
        except NoSuchElementException:
                return None
    # Reset button on create ECDSA parameter page
    def get_ECDSA_reset_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Reset']")
            return element
        except NoSuchElementException:
                return None
    # Objects of ECDSA certificate create page
    def get_ECDSA_generate_cert_link(self):
        try:
            element = self.driver.find_element_by_link_text("Generate ECDSA Self-Signed Certificate and Keys")
            return element
        except NoSuchElementException:
            return None
    #parameter file in certificate creation page
    def get_create_ECDSA_param_file_name_textbox(self):
        try:
            element = self.driver.find_element_by_name('paramfile')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_cert_file_name_textbox(self):
        try:
            element = self.driver.find_element_by_name('certfile')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_private_key_file_name_textbox(self):
        try:
            element = self.driver.find_element_by_name('keyfile')
            return element
        except NoSuchElementException:
            return None

    def get_create_ECDSA_pwd_textbox(self):
        try:
            element = self.driver.find_element_by_name('password')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_confirm_pwd_textbox(self):
        try:
            element = self.driver.find_element_by_name('confirm_password')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_cert_validity_textbox(self):
        try:
            element = self.driver.find_element_by_name('days')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_common_name_textbox(self):
        try:
            element = self.driver.find_element_by_name('cn')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_org_name_textbox(self):
        try:
            element = self.driver.find_element_by_name('o')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_org_unit_name_textbox(self):
        try:
            element = self.driver.find_element_by_name('ou')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_locality_textbox(self):
        try:
            element = self.driver.find_element_by_name('l')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_state_textbox(self):
        try:
            element = self.driver.find_element_by_name('st')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_country_textbox(self):
        try:
            element = self.driver.find_element_by_name('c')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_email_textbox(self):
        try:
            element = self.driver.find_element_by_name('emailAddress')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_state_textbox(self):
        try:
            element = self.driver.find_element_by_name('st')
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_SHA1_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_SHA224_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha224']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_SHA256_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha256']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_SHA384_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha384']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_SHA512_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha512']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_SHA1_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_gen_cert_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Generate Certificate and Key']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ECDSA_reset_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Reset']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_cotinue_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Continue']")
            return element
        except NoSuchElementException:
            return None
    # Page Objects for 	Generate ECDSA Certificate Signing Request (CSR) and Keys
    def get_create_ESDSA_CSR_link(self):
        try:
            element = self.driver.find_element_by_link_text("Generate ECDSA Certificate Signing Request (CSR) and Keys")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_paramfile_textbox(self):
        try:
            element = self.driver.find_element_by_name("paramfile")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_certfile_textbox(self):
        try:
            element = self.driver.find_element_by_name("csrfile")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_keyfile_textbox(self):
        try:
            element = self.driver.find_element_by_name("keyfile")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_pwd_textbox(self):
        try:
            element = self.driver.find_element_by_name("password")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_conpwd_textbox(self):
        try:
            element = self.driver.find_element_by_name("confirm_password")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_comname_textbox(self):
        try:
            element = self.driver.find_element_by_name("cn")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_orgname_textbox(self):
        try:
            element = self.driver.find_element_by_name("o")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_orgunitname_textbox(self):
        try:
            element = self.driver.find_element_by_name("ou")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_loc_textbox(self):
        try:
            element = self.driver.find_element_by_name("l")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_state_textbox(self):
        try:
            element = self.driver.find_element_by_name("st")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_country_textbox(self):
        try:
            element = self.driver.find_element_by_name("c")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_email_textbox(self):
        try:
            element = self.driver.find_element_by_name("emailAddress")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_SHA1_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_SHA224_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha224']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_SHA256_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha256']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_SHA384_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha384']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_SHA512_radiobutton(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='sha512']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_genCSR_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Generate ECDSA CSR']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_reset_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Reset']")
            return element
        except NoSuchElementException:
            return None
    def get_create_ESDSA_CSR_continue_button(self):
        try:
            element = self.driver.find_element_by_xpath("//input[@value='Continue']")
            return element
        except NoSuchElementException:
            return None
    def wait_for_sail_page_to_load(self):
        wait = WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_link_text('Configuration')))
    def wait_for_cert_create_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_link_text('Generate ECDSA Parameters')))
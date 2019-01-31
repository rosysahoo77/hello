import pytest
from selenium.webdriver import Firefox,Chrome,Ie

def get_driver_instance():
    browser = pytest.config.option.browser.lower()
    url = pytest.config.option.server.lower()

    if browser == 'firefox':
        driver = Firefox("./browser-servers/geckodriver.exe")
    elif browser == 'chrome':
        driver = Chrome("./browser-servers/chromedriver.exe")
    elif browser == 'ie':
        driver = Ie("./browser-servers/IEDriverServer.exe")
    else:
        print('invalid browser option')
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url== 'prod':
        driver.get('https://10.62.144.143:57302/')
    else:
        driver.get("https://10.62.144.143:57302/")
    return driver

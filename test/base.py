import unittest

from selenium.webdriver.chrome import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.ChromiumDriver()
        self.driver.implicitly_wait(30)
        self.url = ""
        self.verificationErrors = []
        self.accept_next_alert = True


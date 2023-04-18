import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = ""
        self.verificationErrors = []
        self.accept_next_alert = True


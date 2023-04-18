import unittest
import logging

from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = ""
        self.verificationErrors = []
        self.accept_next_alert = True


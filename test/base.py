import logging
import unittest

from main.utils import webdrivermgr


class BaseTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.logger = logging.getLogger(__name__)
        cls.driver = webdrivermgr.create_chromedriver()
        cls.driver.implicitly_wait(30)
        cls.url = ""
        cls.verificationErrors = []
        cls.accept_next_alert = True

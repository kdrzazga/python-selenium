from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage
from main.utils.files import read_yaml_file


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.subheader = None  # declaration
        self.header = None
        self.url = read_yaml_file()["url"]["the-internet"]["main-page"]
        self.driver = driver

    def find_elements(self):
        self.header = self.driver.find_element(By.TAG_NAME, 'h1')
        self.subheader = self.driver.find_element(By.TAG_NAME, 'h2')

    def check_header(self, expected_text):
        actual_text = self.header.text
        assert actual_text == expected_text, f'Header text "{actual_text}" does not match expected text "{expected_text}"'

    def check_subheader(self, expected_text):
        actual_text = self.subheader.text
        assert actual_text == expected_text, f'Subheader text "{actual_text}" does not match expected text "{expected_text}"'

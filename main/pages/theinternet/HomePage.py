from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage
from main.utils.files import read_yaml_file
from main.utils.locators_helper import quietly_find_element


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.subheader = None #declaration
        self.header = None
        self.url = read_yaml_file()["url"]["the-internet"]["main-page"]

    def find_elements(self):
        self.wait_for_element(By.CSS_SELECTOR, "h1")
        self.header = self.driver.find_element(By.CSS_SELECTOR, "h1")
        self.wait_for_element(By.CSS_SELECTOR, "h2")
        self.subheader = self.driver.find_element(By.CSS_SELECTOR, "h2")

    def check_header(self, expected_text):
        actual_text = self.header.text
        assert actual_text == expected_text, f'Header text "{actual_text}" does not match expected text "{expected_text}"'

    def check_subheader(self, expected_text):
        actual_text = self.subheader.text
        assert actual_text == expected_text, f'Subheader text "{actual_text}" does not match expected text "{expected_text}"'

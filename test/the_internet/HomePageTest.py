from loguru import logger

from main.pages.theinternet.HomePage import HomePage
from test.base import BaseTest


class HomePageTest(BaseTest):
    def __init__(self, method_name: str) -> None:
        super().__init__(methodName=method_name)
        super().setUp()
        self._home_page = HomePage(self.driver)

    def test_navigate(self):
        self.driver.get(self._home_page.url)
        logger.info("Page title: " + self.driver.title)
        self.assertEquals("The Internet", self.driver.title)

    def test_headers(self):
        self.driver.get(self._home_page.url)
        self._home_page.find_elements()
        self._home_page.check_header("Welcome to the-internet")
        self._home_page.check_subheader("Available Examples")

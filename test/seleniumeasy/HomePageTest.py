from main.pages.seleniumeasy.HomePage import HomePage
from test.base import BaseTest


class HomePageTest(BaseTest):
    def __init__(self, method_name: str) -> None:
        super().__init__(methodName=method_name)
        self._home_page = HomePage()

    def test_navigate(self):
        self.driver.get(self._home_page.url)

        self.assertIn(self, "Selenium Easy", self.driver.title)

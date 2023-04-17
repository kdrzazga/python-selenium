from main.pages.seleniumeasy.HomePage import HomePage
from test.base import BaseTest


class HomePageTest(BaseTest):

    def __init__(self):
        super(HomePageTest, self).__init__()
        self._home_page = HomePage()

    def test_navigate(self):
        self.driver.get(self._home_page._url)

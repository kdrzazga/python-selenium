from main.pages.BasePage import BasePage
from main.utils.files import read_yaml_file


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.url = read_yaml_file()["url"]["selenium-easy"]["main-page"]

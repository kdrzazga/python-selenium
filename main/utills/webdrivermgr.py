import logging
import os

from selenium.webdriver.chrome import webdriver

from main.utills.files import read_yaml_file


def create_chromedriver():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    chrome_drv_path = read_yaml_file()
    os.environ["webdriver.chrome.driver"] = chrome_drv_path
    return webdriver.ChromiumDriver(chrome_drv_path)

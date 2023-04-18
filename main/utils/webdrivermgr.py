import os

from loguru import logger
from selenium import webdriver

from main.utils.files import read_yaml_file


def create_chromedriver():
    chrome_drv_path = read_yaml_file()["path"]["chromedriver"]
    logger.info("Path to chromedriver: " + chrome_drv_path)
    os.environ["webdriver.chrome.driver"] = chrome_drv_path
    return webdriver.Chrome(chrome_drv_path)

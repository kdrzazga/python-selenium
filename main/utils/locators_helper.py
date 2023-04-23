from loguru import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def quietly_find_element(driver: WebDriver, by, timeout: int) -> WebElement:
    wait = WebDriverWait(driver, timeout)
    try:
        element_located = ec.presence_of_element_located(by)
        element = wait.until(element_located, "element not found")
        logger.info("Element found" + by)
        return element

    except NoSuchElementException:
        logger.error("Element not found" + by)
        return None

    except TimeoutException:
        logger.error("Timeout Exception for " + by)
        return None

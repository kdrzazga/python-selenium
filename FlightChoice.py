from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PageBase import PageBase

class FlightsPage(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)
        self.wait_for_element(By.TAG_NAME, 'flights-table')

    def select_first_flight(self):
        self.wait_for_element(By.CLASS_NAME, 'flight')
        flight_elements = self.driver.find_elements_by_class_name('flight')
        flight_element = flight_elements[0]

        regular_price_element = flight_element.find_element_by_class_name('regular')

        radio_element = regular_price_element.find_element_by_class_name('core-radio')
        self.focus_element(radio_element)

    def click_continue(self):
        continue_button_element = self.wait_for_element_clickable(By.XPATH, "//div[@class='button-next']/button[@id='continue']")
        time.sleep(5) #if we do the whole booking to fast, we get the 'session expired error'
        continue_button_element.click()

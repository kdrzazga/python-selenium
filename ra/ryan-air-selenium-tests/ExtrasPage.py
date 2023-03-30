from selenium.webdriver.common.by import By
from PageBase import PageBase

class ExtrasPage(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)

    def check_out(self):
        continue_button_element = self.wait_for_element_clickable(By.XPATH,
                                                        "//div[@class='button-next']/button[@translate='trips.summary.buttons.btn_checkout']")
        self.focus_element(continue_button_element)

        popup_ok_button = self.wait_for_element(By.XPATH, "//button[@translate='trips.summary.seat.prompt.popup.reject']")
        self.focus_element(popup_ok_button)

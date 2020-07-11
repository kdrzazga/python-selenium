from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from PageBase import PageBase

class PaymentPage(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)
        
    def select_title(self, index):
        option_element = self.wait_for_element(By.XPATH, "//div[@class='core-select']/select")
        self.focus_element(option_element)
        while index > 0:
            option_element.send_keys(Keys.ARROW_DOWN)
            index = index - 1
            
    def enter_first_name(self, fist_name):
        self.enter_name('first-name', fist_name)
        
    def enter_last_name(self, last_name):
        self.enter_name('last-name', last_name)
        
    def enter_name(self, sufix, name):
        first_name_input = self.wait_for_element(By.XPATH, "//div[@class='form-field payment-passenger-%s']/input" % sufix)
        self.focus_element(first_name_input)
        first_name_input.send_keys(name)

    def enter_email(self, email):
        email_input = self.wait_for_element(By.XPATH, "//div[contains(@class, 'contact-details-email')]/input")
        self.focus_element(email_input)
        email_input.send_keys(email)

        confirm_email_input = self.wait_for_element(By.XPATH, "//div[contains(@class, 'contact-details-confirm-email')]/input")
        self.focus_element(confirm_email_input)
        confirm_email_input.send_keys(email)

    def enter_phone(self, country, phone_number):
        phone_number_country_select = self.wait_for_element(By.NAME, 'phoneNumberCountry')
        self.focus_element(phone_number_country_select)
        phone_number_country_select.send_keys(country)

        phone_number_input = self.wait_for_element(By.XPATH, "//div[@class='phone-number']/input")
        self.focus_element(phone_number_input)
        phone_number_input.send_keys(phone_number)

    def enter_card(self, card_number, type, expiry_month, expiry_year, cvv, cardholder):
        self.send_keys(self.get_core_input_element('card-seats-flow'), card_number)

        card_type_select = self.wait_for_element(By.XPATH, "//div[contains(@class, 'card-type-select')]/select")
        self.focus_element(card_type_select)
        card_type_select.send_keys(type)
        
        self.send_keys(self.get_core_select_element('date-expiry-left'), expiry_month)

        self.send_keys(self.get_core_select_element('date-expiry-right'), expiry_year)

        self.send_keys(self.get_core_input_element('card-security-code'), cvv)
        
        self.send_keys(self.get_core_input_element('cardholders-name'), cardholder)

    def enter_billing_address(self, address1, city):
        self.send_keys(self.get_core_input_element('address-line-1'), address1)
        self.send_keys(self.get_core_input_element('city'), city)
        
    def press_pay_now(self):
        self.focus_element(self.get_core_input_element('terms'))
    
        pay_now_button = self.wait_for_element_clickable(By.XPATH, "//button[@translate='common.components.payment_forms.pay_now']")
        self.focus_element(pay_now_button)

    def was_payment_declined(self):
        try:
            error_message_pane = self.wait_for_element(By.XPATH, "//div[@translate='common.components.payment_forms.error_explain_declined']")
        except TimeoutException:
            return False
        if "As your payment was not authorised we could not complete your reservation" in error_message_pane.get_attribute('innerHTML'): #this is done because that was requested in the task contents
            return True
        else:
            return False

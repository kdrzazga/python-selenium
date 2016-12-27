import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Page
import FlightChoice
import ExtrasPage
import PaymentPage
import time

#TODO: generalise page classes so that it's possible for example to chose flight type (regular/plus/business plus)

chrome_drv_path = 'chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chrome_drv_path
driver = webdriver.Chrome(chrome_drv_path)
url = 'http://www.ryanair.com/ie/en/'

main_page = Page.MainPage(driver, url)
main_page.open()
main_page.choose_ticket_type('oneWay')
main_page.choose_airport('departure', 'Warsaw (WMI)')
main_page.choose_airport('destination', 'London Stansted')
main_page.click_continue()
main_page.set_departure_date()

flights_page = FlightChoice.FlightsPage(driver)
flights_page.select_first_flight()
flights_page.click_continue()

extras_page = ExtrasPage.ExtrasPage(driver)
extras_page.check_out()

payment_page = PaymentPage.PaymentPage(driver)
payment_page.select_title(1)
payment_page.enter_first_name('Liliana')
payment_page.enter_last_name('Niewiadomska')
payment_page.enter_email('asdf@gmail.pl')
payment_page.enter_phone('Poland', '567456789')
payment_page.enter_card('4485142134218326', 'Visa', '1', '2019', '123', 'Liliana Niewiadomska') #other card numbers: 4556660773103602, 4556375702257680, 4916066237707563
payment_page.enter_billing_address('WebDriver Street 2016', 'Dublin')
payment_page.press_pay_now()

assert payment_page.was_payment_declined()

time.sleep(10) #time to notice the result
driver.quit()

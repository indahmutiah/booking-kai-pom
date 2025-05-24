from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.booking import Locator

class BookingPage:
    def __init__(self, setup):
        self.setup = setup

    def set_departure(self, departure):
        self.setup.find_element(*Locator.input_depature).send_keys(departure)
        self.setup.find_element(*Locator.departure_dropdown).click()
        self.setup.find_element(*Locator.departure_list)[0].click()
    
    def set_arrival(self, arrival):
        self.setup.find_element(*Locator.arrival_input).send_keys(arrival)
        self.setup.find_element(*Locator.arrival_dropdown).click()
        self.setup.find_element(*Locator.arrival_list)[0].click()
    
    def select_holiday(self):
        self.setup.find_element(*Locator.departure_date).click()
        try:
            self.wait.until(EC.presence_of_element_located(Locator.date_picker))
            holiday = self.setup.find_elements(*Locator.holiday_date)
            if holiday:
                holiday[0].click()
        except TimeoutException:
            pass
    
    def submit(self):
        self.setup.find_element(*Locator.submit_btn).click()
from selenium.webdriver.common.by import By

class Locator:
    input_depature = (By.ID, "origination-flexdatalist")
    departure_dropdown = (By.ID, "origination-flexdatalist-results")
    departure_list = (By.CSS_SELECTOR, "#origination-flexdatalist-results li.item")

    arrival_input = (By.ID, "destination-flexdatalist")
    arrival_dropdown = (By.ID, "destination-flexdatalist-results")
    arrival_list = (By.CSS_SELECTOR, "#destination-flexdatalist-results li.item")

    departure_date = (By.XPATH, "//input[@id='departure_dateh']")
    date_picker = (By.ID, "ui-datepicker-div")
    holiday_date =  (By.XPATH, '//td[@class=" holiday"]')

    submit_btn= (By.XPATH, '//input[@id="submit"]')
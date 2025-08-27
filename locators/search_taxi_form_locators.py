from selenium.webdriver.common.by import By

class SearchTaxiFormLocators:

    TITLE_TAXI = (By.XPATH, ".//*[@class='order-header-title']")
    TIMER_TAXI = (By.XPATH, ".//*[@class='order-header-time']")

    BUTTON_RETURN = (By.XPATH, ".//div[text()='Отменить']/../button")
    TEXT_BUTTON_RETURN = (By.XPATH, ".//div[text()='Отменить']")

    BUTTON_DETAILS = (By.XPATH, ".//div[text()='Детали']/../button")
    TEXT_BUTTON_DETAILS = (By.XPATH, ".//div[text()='Детали']")
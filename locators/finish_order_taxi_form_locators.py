from selenium.webdriver.common.by import By

class FinishOrderTaxiFormLocators:

    TITLE_FORM = (By.XPATH, ".//*[@class='order-header-title']")

    PICTURE_TAXI = (By.XPATH, ".//img[@alt='Car']")
    CAR_NUMBER_TAXI = (By.XPATH, ".//*[@class='number']")

    PICTURE_CAR_DRIVER = (By.XPATH, ".//*[@class='order-btn-rating']/../img")
    RATING_CAR_DRIVER = (By.XPATH, ".//*[@class='order-btn-rating']")
    NAME_CAR_DRIVER = (By.XPATH, ".//*[@class='order-btn-rating']/../../div[2]")

    BUTTON_RETURN = (By.XPATH, ".//div[text()='Отменить']/../button")
    TEXT_BUTTON_RETURN = (By.XPATH, ".//div[text()='Отменить']")

    BUTTON_DETAILS = (By.XPATH, ".//div[text()='Детали']/../button")
    TEXT_BUTTON_DETAILS = (By.XPATH, ".//div[text()='Детали']")

    TEXT_PRICE = (By.XPATH, ".//*[text()='Стоимость - ']")
    TIMER_TAXI = (By.XPATH, ".//*[@class='order-header-time']")
from selenium.webdriver.common.by import By

class GetTaxiLocators:

    TAXI_TARIFFS_NAMES_LIST = (By.XPATH, ".//div[@class='tcard-title']")

    ACTIVE_TARIFF_NAME = (By.XPATH, ".//div[@class='tcard active']/div[@class='tcard-title']")
    ACTIVE_BUTTON_INFO = (By.XPATH, ".//div[@class='tcard active']/button[@class = 'i-button tcard-i active']")
    ACTIVE_TITLE_INFO = (By.XPATH, ".//div[@class='tcard active']//div[@class = 'i-title']")
    ACTIVE_DESCRIPTION_INFO = (By.XPATH, ".//div[@class='tcard active']//div[@class = 'i-dPrefix']")
    ACTIVE_PRICE_INFO = (By.XPATH, ".//div[@class='tcard active']//div[@class = 'tcard-price']")

    BUTTON_TARIFF_WORK = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Рабочий']")
    BUTTON_TARIFF_SLEEP = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Сонный']")
    BUTTON_TARIFF_VACATION = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Отпускной']")
    BUTTON_TARIFF_TALK = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Разговорчивый']")
    BUTTON_TARIFF_COMFORTING = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Утешительный']")
    BUTTON_TARIFF_GLOSSY = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Глянцевый']")

    EXTRA_INFO_PANEL = (By.XPATH, ".//*[@class='tariff-picker shown']")
    EXTRA_INPUT_PHONE = (By.CLASS_NAME, "np-text")
    EXTRA_BUTTON_PAYMENT_METHOD = (By.CLASS_NAME, "pp-text")
    EXTRA_INPUT_COMMENT = (By.XPATH, ".//input[@id='comment']/../label")
    EXTRA_TITLE_REQUIREMENTS = (By.CLASS_NAME, 'reqs-head')
    EXTRA_BUTTON_GET_TAXI = (By.CLASS_NAME, "smart-button-main")
    EXTRA_ICON_ARROW_REQUIREMENTS = (By.CLASS_NAME, 'reqs-head')
    EXTRA_SWITCH_LAPTOP = (By.XPATH, ".//*[@class='slider round']")

from selenium.webdriver.common.by import By

class MainPageLocators:

    INPUT_ADDRESS_FROM = (By.ID, "from")
    INPUT_ADDRESS_TO = (By.ID, "to")
    POINTS_ADDRESS = (By.XPATH, ".//ymaps[contains(@class, 'ymaps-2-1-79-route-pin__text')]/ymaps[@id]")

    PANEL_CHOOSE_ROUTE = (By.XPATH, ".//div[@class='type-picker shown']")
    TABS_ROUTE = (By.XPATH, ".//div[@class='modes-container']/div[contains(@class, 'mode')]")
    TEXT_DESCRIPTION = (By.CLASS_NAME, "text")
    TEXT_DURATION = (By.CLASS_NAME, "duration")
    TAB_ACTIVE = (By.XPATH, ".//div[@class='mode active']")
    BUTTON_GET_TAXI = (By.XPATH, ".//div[@class = 'results-container']//button")

    OPTION_CAR = (By.XPATH, ".//img[contains(@src, 'car.')]/..")
    OPTION_WALK = (By.XPATH, ".//img[contains(@src, 'walk')]/..")
    OPTION_TAXI = (By.XPATH, ".//img[contains(@src, 'taxi')]/..")
    OPTION_BICYCLE = (By.XPATH, ".//img[contains(@src, 'bike')]/..")
    OPTION_SCOOTER = (By.XPATH, ".//img[contains(@src, 'scooter')]/..")
    OPTION_DRIVE = (By.XPATH, ".//img[contains(@src, 'drive')]/..")
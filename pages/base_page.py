from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from data.urls import Urls
import allure

class BasePage:
    
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.URL_BASE = Urls.BASE_URL
        
    @allure.step("Открытие страницы главной страницы")
    def open(self):
        self.driver.get(self.URL_BASE)
        
    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Дождаться кликабельности элмента {locator}")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        self.wait_for_clickable(locator).click()
        
    @allure.step("Нажать на элемент без локатора")
    def click_element_without_locator(self, element):
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step("Заполнить поле")
    def send_keys_to_element(self, locator, keys):
        self.wait_for_clickable(locator).send_keys(keys)
        
    @allure.step("Дождаться изменения текста")
    def wait_change_of_element(self, locator, text_must_change):
        self.wait_for_visible(locator)
        self.find_element(locator)
        WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(locator, str(text_must_change)))
        
    @allure.step("Дождаться появления текста")
    def wait_text_is_visible(self, locator, text_must_visible):
        WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element(locator, text_must_visible))
        
    @allure.step("Получить текст элемента")
    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Получить текст без локатора")
    def get_text_from_element_without_locator(self, element):
        self.wait.until(EC.visibility_of(element))
        return element.text
    
    @allure.step("Навести курсор на элемент {locator}")
    def focus_on_element(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()
        
    @allure.step("Ожидание видимости элемента")
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutError:
            return False
        
    @allure.step("Ожидание исчезновения элемента")
    def is_element_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(locator))
            return True
        except TimeoutError:
            return False
        
    @allure.step("Элемент не задизейблен")
    def is_element_not_disable(self, locator):
        element = self.find_element(locator)
        class_attribute_list = element.get_attribute("class")
        if "disabled" not in class_attribute_list:
            return True
        else:
            return False
        
    @allure.step("Скролл к элементу {locator}")
    def move_to_down_in_container(self, container_locator):
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container_locator)
from locators.get_taxi_locators import GetTaxiLocators
from pages.base_page import BasePage
from data.data import Data
import allure

class GetTaxiPage(BasePage):
    
    @allure.step("Получение имени активного тарифа")
    def get_name_active_tariff(self):
        self.wait_for_visible(GetTaxiLocators.ACTIVE_TARIFF_NAME)
        return self.get_text_from_element(GetTaxiLocators.ACTIVE_TARIFF_NAME)
    
    @allure.step("Получение списка имен всех тарифов")
    def get_list_names_all_tariffs(self):
        self.wait_for_visible(GetTaxiLocators.TAXI_TARIFFS_NAMES_LIST)
        elements = self.driver.find_elements(*GetTaxiLocators.TAXI_TARIFFS_NAMES_LIST)
        return [element.text for element in elements]    
    
    @allure.step("Сравнение списка имен всех тарифов с эталонным")
    def compare_list_names_all_tariffs(self):
        list_names_all_tariffs = self.get_list_names_all_tariffs()
        for tarif in Data.LIST_TARIFFS_NAMES:
            if tarif not in list_names_all_tariffs:
                return False
        return True
    
    @allure.step("Активный тариф выделен в списке тарифов")
    def is_active_tariff_highlighted(self):
        active_tariff = self.get_name_active_tariff()
        all_tariffs = self.get_list_names_all_tariffs()
        if active_tariff in all_tariffs:
            return True
        
        return False
    
    @allure.step("Нажать на тариф рабочий")
    def click_button_tariff_work(self):
        self.click_element(GetTaxiLocators.BUTTON_TARIFF_WORK)
        
    @allure.step("Нажать на тариф сонный")
    def click_button_tariff_sleep(self):
        self.click_element(GetTaxiLocators.BUTTON_TARIFF_SLEEP)
        
    @allure.step("Нажать на тариф отпускной")
    def click_button_tariff_vacation(self):
        self.click_element(GetTaxiLocators.BUTTON_TARIFF_VACATION)
        
    @allure.step("Нажать на тариф разговорчивый")
    def click_button_tariff_talk(self):
        self.click_element(GetTaxiLocators.BUTTON_TARIFF_TALK)
        
    @allure.step("Нажать на тариф утешительный")
    def click_button_tariff_comforting(self):
        self.click_element(GetTaxiLocators.BUTTON_TARIFF_COMFORTING)
        
    @allure.step("Нажать на тариф глянцевый")
    def click_button_tariff_glossy(self):
        self.click_element(GetTaxiLocators.BUTTON_TARIFF_GLOSSY)
        
    @allure.step("Навести курсор на иконку информации")
    def focus_on_button_info(self):
        self.focus_on_element(GetTaxiLocators.ACTIVE_BUTTON_INFO)
        
    @allure.step("Окно с подсказкой появилось")
    def is_extra_info_panel_visible(self):
        return self.is_element_visible(GetTaxiLocators.EXTRA_INFO_PANEL)
    
    @allure.step("Получение заголовка подсказки")
    def get_info_title(self):
        self.wait_for_visible(GetTaxiLocators.ACTIVE_TITLE_INFO)
        return self.get_text_from_element(GetTaxiLocators.ACTIVE_TITLE_INFO)
    
    @allure.step("Получение описания подсказки")
    def get_info_description(self):
        self.wait_for_visible(GetTaxiLocators.ACTIVE_DESCRIPTION_INFO)
        return self.get_text_from_element(GetTaxiLocators.ACTIVE_DESCRIPTION_INFO)
    
    @allure.step("Получение текста поля 'телефон'")
    def get_text_input_phone(self):
        self.wait_for_visible(GetTaxiLocators.EXTRA_INPUT_PHONE)
        return self.get_text_from_element(GetTaxiLocators.EXTRA_INPUT_PHONE)
    
    @allure.step("Получение текста кнопки 'способ оплаты'")
    def get_text_button_payment_method(self):
        self.wait_for_visible(GetTaxiLocators.EXTRA_BUTTON_PAYMENT_METHOD)
        return self.get_text_from_element(GetTaxiLocators.EXTRA_BUTTON_PAYMENT_METHOD)
    
    @allure.step("Получение текста поля 'комментарий водителю'")
    def get_text_input_comment(self):
        self.wait_for_visible(GetTaxiLocators.EXTRA_INPUT_COMMENT)
        return self.get_text_from_element(GetTaxiLocators.EXTRA_INPUT_COMMENT)
    
    @allure.step("Получение заголовка 'требования к заказу'")
    def get_text_title_requirements(self):
        self.wait_for_visible(GetTaxiLocators.EXTRA_TITLE_REQUIREMENTS)
        return self.get_text_from_element(GetTaxiLocators.EXTRA_TITLE_REQUIREMENTS)
    
    @allure.step("Получение текста кнопки 'ввести номер и заказать'")
    def get_text_button_get_taxi(self):
        self.wait_for_visible(GetTaxiLocators.EXTRA_BUTTON_GET_TAXI)
        return self.get_text_from_element(GetTaxiLocators.EXTRA_BUTTON_GET_TAXI)
    
    @allure.step("Нажать на иконку стрелки 'требования к заказу'")
    def click_icon_arrow_requirements(self):
        self.click_element(GetTaxiLocators.EXTRA_ICON_ARROW_REQUIREMENTS)
        
    @allure.step("Скролл к низу страницы")
    def scroll_to_bottom_page(self):
        extra_bottom = self.find_element(GetTaxiLocators.EXTRA_INFO_PANEL)
        self.move_to_down_in_container(extra_bottom)
        
    @allure.step("Переключить свитчер 'ноутбук/телефон'")
    def switch_laptop_table(self):
        self.click_element(GetTaxiLocators.EXTRA_SWITCH_LAPTOP)
        
    @allure.step("Нажать на кнопку 'ввести номер и заказать'")
    def click_button_get_taxi(self):
        self.click_element(GetTaxiLocators.EXTRA_BUTTON_GET_TAXI)
        
    @allure.step("Получить стоимость маршрута")
    def get_text_price_info(self):
        price = self.get_text_from_element(GetTaxiLocators.ACTIVE_PRICE_INFO)
        return price.replace(' ', '')
    
from locators.search_taxi_form_locators import SearchTaxiFormLocators
from pages.base_page import BasePage
import allure

class SearchTaxiFormPage(BasePage):
    
    @allure.step("Получение текста заголовка формы поиска такси")
    def get_text_title_search_taxi_form(self):
        self.wait_for_visible(SearchTaxiFormLocators.TITLE_TAXI)
        return self.get_text_from_element(SearchTaxiFormLocators.TITLE_TAXI)
    
    @allure.step("Получение текста кнопки 'Отменить'")
    def get_text_button_return(self):
        self.wait_for_visible(SearchTaxiFormLocators.TEXT_BUTTON_RETURN)
        return self.get_text_from_element(SearchTaxiFormLocators.TEXT_BUTTON_RETURN)
    
    @allure.step("Нажать на кнопку 'Отменить'")
    def click_button_return(self):
        self.click_element(SearchTaxiFormLocators.BUTTON_RETURN)
        
    @allure.step("Получение текста кнопки 'Детали'")
    def get_text_button_details(self):
        self.wait_for_visible(SearchTaxiFormLocators.TEXT_BUTTON_DETAILS)
        return self.get_text_from_element(SearchTaxiFormLocators.TEXT_BUTTON_DETAILS)
    
    @allure.step("Нажать на кнопку 'Детали'")
    def click_button_details(self):
        self.click_element(SearchTaxiFormLocators.BUTTON_DETAILS)
        
    @allure.step("Таймер обратного отсчета отображается")
    def is_timer_visible(self):
        return self.is_element_visible(SearchTaxiFormLocators.TIMER_TAXI)
    
    @allure.step("Ожидание окончания таймера")
    def wait_timer_end(self):
        self.wait_text_is_visible(SearchTaxiFormLocators.TIMER_TAXI, "00:01")
        self.wait_change_of_element(SearchTaxiFormLocators.TIMER_TAXI, "00:01")
    
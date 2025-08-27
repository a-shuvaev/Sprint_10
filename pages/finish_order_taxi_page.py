from locators.finish_order_taxi_form_locators import FinishOrderTaxiFormLocators
from pages.base_page import BasePage
import allure

class FinishOrderTaxiPage(BasePage):
    
    @allure.step("Получение текста заголовка формы завершения заказа такси")
    def get_text_title_finish_order_taxi_form(self):
        self.wait_for_visible(FinishOrderTaxiFormLocators.TITLE_FORM)
        return self.get_text_from_element(FinishOrderTaxiFormLocators.TITLE_FORM)
    
    @allure.step("Картинка с машиной такси отображается")
    def is_picture_taxi_visible(self):
        return self.is_element_visible(FinishOrderTaxiFormLocators.PICTURE_TAXI)
    
    @allure.step("Отображается валидный номер телефона")
    def is_car_number_taxi_valid(self):
        self.wait_for_visible(FinishOrderTaxiFormLocators.CAR_NUMBER_TAXI)
        car_number = self.get_text_from_element(FinishOrderTaxiFormLocators.CAR_NUMBER_TAXI)
        if len(car_number) == 8:
            return True
        return False
    
    @allure.step("Аватар водителя отображается")
    def is_picture_car_driver_visible(self):
        return self.is_element_visible(FinishOrderTaxiFormLocators.PICTURE_CAR_DRIVER)
    
    @allure.step("Рейтинг водителя отображается")
    def is_rating_car_driver_visible(self):
        return self.is_element_visible(FinishOrderTaxiFormLocators.RATING_CAR_DRIVER)
    
    @allure.step("Имя водителя отображается")
    def is_name_car_driver_visible(self):
        return self.is_element_visible(FinishOrderTaxiFormLocators.NAME_CAR_DRIVER)
    
    @allure.step("Аватар водителя не отображается")
    def is_picture_car_driver_invisible(self):
        return self.is_element_invisible(FinishOrderTaxiFormLocators.PICTURE_CAR_DRIVER)
    
    @allure.step("Получение текста кнопки 'Отменить'")
    def get_text_button_return(self):
        self.wait_for_visible(FinishOrderTaxiFormLocators.TEXT_BUTTON_RETURN)
        return self.get_text_from_element(FinishOrderTaxiFormLocators.TEXT_BUTTON_RETURN)
    
    @allure.step("Нажать на кнопку 'Отменить'")
    def click_button_return(self):
        self.click_element(FinishOrderTaxiFormLocators.BUTTON_RETURN)
    
    @allure.step("Получение текста кнопки 'Детали'")
    def get_text_button_details(self):
        self.wait_for_visible(FinishOrderTaxiFormLocators.TEXT_BUTTON_DETAILS)
        return self.get_text_from_element(FinishOrderTaxiFormLocators.TEXT_BUTTON_DETAILS)
    
    @allure.step("Нажать на кнопку 'Детали'")
    def click_button_details(self):
        self.click_element(FinishOrderTaxiFormLocators.BUTTON_DETAILS)
        
    @allure.step("Получение текста стоимости поездки")
    def get_text_price(self):
        self.wait_for_visible(FinishOrderTaxiFormLocators.TEXT_PRICE)
        return self.get_text_from_element(FinishOrderTaxiFormLocators.TEXT_PRICE)
    
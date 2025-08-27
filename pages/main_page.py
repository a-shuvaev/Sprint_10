from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    
    @allure.step("Ввод адреса в поле Откуда")
    def input_address_from(self, address):
        self.send_keys_to_element(MainPageLocators.INPUT_ADDRESS_FROM, address)
        
    @allure.step("Ввод адреса в поле Куда")
    def input_address_to(self, address):
        self.send_keys_to_element(MainPageLocators.INPUT_ADDRESS_TO, address)
        
    @allure.step("Получение точек на карте")
    def get_list_points_on_map(self):
        self.wait_for_visible(MainPageLocators.POINTS_ADDRESS)
        return self.driver.find_elements(*MainPageLocators.POINTS_ADDRESS)
    
    @allure.step("Получение списка табов выбора маршрута")
    def get_list_tabs_route(self):
        self.wait_for_visible(MainPageLocators.PANEL_CHOOSE_ROUTE)
        return self.driver.find_elements(*MainPageLocators.TABS_ROUTE)
    
    @allure.step("Нажатие на таб 'оптимальный'")
    def click_tab_optimal(self):
        tab = self.get_list_tabs_route()[0]
        self.click_element_without_locator(tab)
    
    @allure.step("Получение текста таба 'оптимальный'")
    def get_text_tab_optimal(self):
        tab = self.get_list_tabs_route()[0]
        self.get_text_from_element_without_locator(tab)
        
    @allure.step("Нажатие на таб 'быстрый'")
    def click_tab_fast(self):
        tab = self.get_list_tabs_route()[1]
        self.click_element_without_locator(tab)
        
    @allure.step("Получение текста таба 'быстрый'")
    def get_text_tab_fast(self):
        tab = self.get_list_tabs_route()[1]
        self.get_text_from_element_without_locator(tab)
        
    @allure.step("Нажатие на таб 'свой'")
    def click_tab_self(self):
        tab = self.get_list_tabs_route()[2]
        self.click_element_without_locator(tab)
        
    @allure.step("Получение текста таба 'свой'")
    def get_text_tab_self(self):
        tab = self.get_list_tabs_route()[2]
        self.get_text_from_element_without_locator(tab)
        
    @allure.step("Проверка видимости панели выбора маршрута")
    def is_panel_choose_route_visible(self):
        return self.is_element_visible(MainPageLocators.PANEL_CHOOSE_ROUTE)
    
    @allure.step("Получение текста стоимости маршрута")
    def get_text_description(self):
        return self.get_text_from_element(MainPageLocators.TEXT_DESCRIPTION)
    
    @allure.step("Получение текста длительности маршрута")
    def get_text_duration(self):
        return self.get_text_from_element(MainPageLocators.TEXT_DURATION)
    
    @allure.step("Получение текста активного таба")
    def get_text_from_active_tab(self):
        return self.get_text_from_element(MainPageLocators.TAB_ACTIVE)
    
    @allure.step("Проверка доступности опции 'авто'")
    def is_option_car_is_not_disabled(self):
        return self.is_element_not_disable(MainPageLocators.OPTION_CAR)
    
    @allure.step("Проверка доступности опции 'пешком'")
    def is_option_walk_is_not_disabled(self):
        return self.is_element_not_disable(MainPageLocators.OPTION_WALK)
    
    @allure.step("Проверка доступности опции 'такси'")
    def is_option_taxi_is_not_disabled(self):
        return self.is_element_not_disable(MainPageLocators.OPTION_TAXI)
    
    @allure.step("Проверка доступности опции 'велосипед'")
    def is_option_bicycle_is_not_disabled(self):
        return self.is_element_not_disable(MainPageLocators.OPTION_BICYCLE)
    
    @allure.step("Проверка доступности опции 'самокат'")
    def is_option_scooter_is_not_disabled(self):
        return self.is_element_not_disable(MainPageLocators.OPTION_SCOOTER)
    
    @allure.step("Проверка доступности опции 'драйв'")
    def is_option_drive_is_not_disabled(self):
        return self.is_element_not_disable(MainPageLocators.OPTION_DRIVE)
    
    @allure.step("Проверка доступности всех опций выбора маршрута")
    def is_all_options_not_disabled(self):
        return (self.is_option_car_is_not_disabled() and
                self.is_option_walk_is_not_disabled() and
                self.is_option_taxi_is_not_disabled() and
                self.is_option_bicycle_is_not_disabled() and
                self.is_option_scooter_is_not_disabled() and
                self.is_option_drive_is_not_disabled())
    
    @allure.step("Нажатие на опцию 'самокат'")
    def click_option_scooter(self):
        self.click_element(MainPageLocators.OPTION_SCOOTER)
        
    @allure.step("Получение текста самоката")
    def get_text_from_button_get_taxi(self):
        return self.get_text_from_element(MainPageLocators.BUTTON_GET_TAXI)
    
    @allure.step("Нажатие на кнопку на панели выбора маршрута")
    def click_on_choose_route_button(self):
        self.click_element(MainPageLocators.PANEL_CHOOSE_ROUTE)
        
    @allure.step("Нажатие на кнопку вызова такси")
    def click_on_button_get_taxi(self):
        self.click_element(MainPageLocators.BUTTON_GET_TAXI)
        
    @allure.step("Нажатие на опцию 'драйв'")
    def click_option_drive(self):
        self.click_element(MainPageLocators.OPTION_DRIVE)
    
    
        
    
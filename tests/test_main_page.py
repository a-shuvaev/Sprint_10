from pages.main_page import MainPage
from data.data import Data
import pytest
import allure

class TestMainPage:
    
    @allure.title("Тест вотображения точек на карте")
    @allure.description("При вводе двух разных предустановленных адресов в поля 'Откуда' и 'Куда' на карте отображаются две точки начала и конца маршрута")
    def test_points_on_map(self, enter_addresses):
        page = MainPage(enter_addresses)
        points = page.get_list_points_on_map()
        
        assert len(points) == 2
        
    @allure.title("Тест отображения панели выбора маршрута")    
    @allure.description("При вводе двух разных предустановленных адресов в поля 'Откуда' и 'Куда' под выбором адресов отображается блок с выбором маршрута")
    def test_panel_choose_route_visible(self, enter_addresses):
        page = MainPage(enter_addresses)
        
        assert page.is_panel_choose_route_visible()
    
    @allure.title("Тест ввода двух одинаковых маршрутов")
    @allure.description("При вводе одинакового адреса в поля 'Откуда' и 'Куда' под выбором адресов отображается блок с выбором маршрута с текстом 'Авто Бесплатно В пути 0 мин.'")
    def test_same_address(self, driver):
        page = MainPage(driver)
        page.input_address_from(Data.ADDRESS_FROM)
        page.input_address_to(Data.ADDRESS_FROM)
        
        assert (page.get_text_description() == Data.TEXT_DESCRIPTION_SAME_ADRESS and
               page.get_text_duration() == Data.TEXT_DURATION_SAME_ADRESS)
    
    @pytest.mark.parametrize('click_tab,get_text_tab',[
        (MainPage.click_tab_optimal, Data.TEXT_TAB_OPTIMAL_ROUTE),
        (MainPage.click_tab_fast, Data.TEXT_TAB_FAST_ROUTE)
    ])
    @allure.title("Тест переключения тарифа на оптимальный/быстрый")
    @allure.description("При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута")
    def test_switch_route_tabs(self, choose_scooter_route, click_tab, get_text_tab):
        page = MainPage(choose_scooter_route)
        
        old_description = page.get_text_description()
        old_duration = page.get_text_duration()
        
        click_tab(page)
        new_tab_title = page.get_text_from_active_tab()
        new_description = page.get_text_description()
        new_duration = page.get_text_duration()
        
        assert (new_tab_title == get_text_tab and
                old_description != new_description and
                old_duration != new_duration)
    
    @allure.title("Тест переключения на маршрут 'Свой'")
    @allure.description("При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)")
    def test_switch_to_self_route_tab(self, enter_addresses):
        page = MainPage(enter_addresses)
        page.click_tab_self()
        
        assert page.is_all_options_not_disabled()
    
    @allure.title("Тест переключения на маршрут 'Быстрый'")
    @allure.description("При выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_switch_to_fast_route_tab(self, enter_addresses):
        page = MainPage(enter_addresses)
        page.click_tab_fast()
        
        assert page.get_text_from_button_get_taxi() == Data.TEXT_GET_TAXI_BUTTON
        
    @allure.title("Тест отображения кнопки 'Забронировать'")
    @allure.description("При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать")
    def test_active_button_book(self, enter_addresses):
        page = MainPage(enter_addresses)
        page.click_tab_self()
        page.click_option_drive()
        
        assert page.get_text_from_button_get_taxi() == Data.TEXT_GET_DRIVE_BUTTON
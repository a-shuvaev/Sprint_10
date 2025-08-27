from pages.search_taxi_form import SearchTaxiFormPage
from pages.get_taxi_page import GetTaxiPage
from data.data import Data
import allure
import pytest

class TestSearchTaxiForm:
    
    @allure.title("Тест отображения формы поиска такси")
    def test_search_taxi_form_visible(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_work()
        page.click_icon_arrow_requirements()
        page.switch_laptop_table()
        page.click_button_get_taxi()
        page = SearchTaxiFormPage(open_panel_tarrif_taxi)
        
        assert page.get_text_title_search_taxi_form() == Data.TEXT_FORM_GET_TAXI
    
    @allure.title("Тест соответствия элементов формы поиска такси ТЗ")
    def test_elements_search_taxi_form(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_work()
        page.click_icon_arrow_requirements()
        page.switch_laptop_table()
        page.click_button_get_taxi()
        page = SearchTaxiFormPage(open_panel_tarrif_taxi)
        
        assert page.get_text_title_search_taxi_form() == Data.TEXT_FORM_GET_TAXI
        assert page.get_text_button_return() == Data.TEXT_FORM_RETURN_BUTTON
        assert page.get_text_button_details() == Data.TEXT_FORM_DETAILS_BUTTON
        assert page.is_timer_visible()
    
    @allure.title("Тест окончания таймера в форме поиска такси")
    def test_timer_end(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_work()
        page.click_icon_arrow_requirements()
        page.switch_laptop_table()
        page.click_button_get_taxi()
        page = SearchTaxiFormPage(open_panel_tarrif_taxi)
        page.wait_timer_end()
        
        assert Data.TEXT_FORM_FINISH_ORDER_TAXI in page.get_text_title_search_taxi_form()
from pages.finish_order_taxi_page import FinishOrderTaxiPage
from pages.search_taxi_form import SearchTaxiFormPage
from pages.get_taxi_page import GetTaxiPage
from data.data import Data
import allure
import pytest

class TestFinishOrderForm:
    
    @allure.title("Тест соответствия элементов формы завершения заказа такси ТЗ")
    def test_elements_finish_order_taxi_form(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_work()
        page.click_icon_arrow_requirements()
        page.switch_laptop_table()
        page.click_button_get_taxi()
        page = SearchTaxiFormPage(open_panel_tarrif_taxi)
        page.wait_timer_end()
        page = FinishOrderTaxiPage(open_panel_tarrif_taxi)
        
        assert Data.TEXT_FORM_FINISH_ORDER_TAXI in page.get_text_title_finish_order_taxi_form()
        assert page.is_picture_taxi_visible()
        assert page.is_car_number_taxi_valid()
        assert page.is_picture_car_driver_visible()
        assert page.is_rating_car_driver_visible()
        assert page.is_name_car_driver_visible()
        assert page.get_text_button_return() == Data.TEXT_FORM_RETURN_BUTTON
        assert page.get_text_button_details() == Data.TEXT_FORM_DETAILS_BUTTON
        
    @allure.title("Тест отображения окна деталей в форме завершения заказа такси")
    def test_open_details_finish_order_taxi_form(self, open_finish_order_taxi_form_with_price):
        finish_driver, cost_old = open_finish_order_taxi_form_with_price
        page = FinishOrderTaxiPage(finish_driver)
        page.click_button_details()
        cost_new = page.get_text_price()
        
        assert cost_old in cost_new, print(cost_old, cost_new)
    
    @pytest.mark.xfail(reason="Нажатие на кнопку 'Отменить' не работает, заведен баг")
    @allure.title("Тест закрытия формы завершения заказа такси по кнопке 'Отменить'")
    def test_close_finish_order_taxi_form(self, open_finish_order_taxi_form):
        page = FinishOrderTaxiPage(open_finish_order_taxi_form)
        page.click_button_return()
        
        assert page.is_picture_car_driver_invisible()
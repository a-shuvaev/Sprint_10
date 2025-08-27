from pages.get_taxi_page import GetTaxiPage
from pages.main_page import MainPage
from data.data import Data
import pytest
import allure

class TestGetTaxiPage:
    
    @allure.title("Тест отображение тарифов такси")
    @allure.description("Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_all_tarrifs_visible(self, enter_addresses):
        page = MainPage(enter_addresses)
        page.click_on_button_get_taxi()
        page = GetTaxiPage(enter_addresses)
        
        assert page.compare_list_names_all_tariffs()
    
    @allure.title("Тест активности тарифа")
    @allure.description("Один тариф выделен как активный")
    def test_active_tarrif(self, enter_addresses):
        page = MainPage(enter_addresses)
        page.click_on_button_get_taxi()
        page = GetTaxiPage(enter_addresses)
        
        assert page.is_active_tariff_highlighted()
        
    @allure.title("Тест отображения тултипа")
    @allure.description("При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ")
    def test_tooltip_tarrif(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.focus_on_button_info()
        
        assert page.is_extra_info_panel_visible()
    
    @allure.title("Тест содержания тултипа для тарифа рабочий")
    def test_tooltip_tarrif_work_texts(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_work()
        page.focus_on_button_info()
        actual_title = page.get_info_title()
        actual_description = page.get_info_description()
        
        assert actual_title == Data.TEXT_TARRIF_WORK['title']
        assert actual_description == Data.TEXT_TARRIF_WORK['description']

    @pytest.mark.xfail(reason="Текст в тултипах тарифов 'Сонный' и 'Разговорчивый' не соответствуют ТЗ, заведен баг")
    @allure.title("Тест содержания тултипа для тарифа сонный")
    def test_tooltip_tarrif_sleep_texts(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_sleep()
        page.focus_on_button_info()
        actual_title = page.get_info_title()
        actual_description = page.get_info_description()
        
        assert actual_title == Data.TEXT_TARRIF_SLEEP['title']
        assert actual_description == Data.TEXT_TARRIF_SLEEP['description']

    @allure.title("Тест содержания тултипа для тарифа отпускной")
    def test_tooltip_tarrif_vacation_texts(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_vacation()
        page.focus_on_button_info()
        actual_title = page.get_info_title()
        actual_description = page.get_info_description()
        
        assert actual_title == Data.TEXT_TARRIF_VACATION['title']
        assert actual_description == Data.TEXT_TARRIF_VACATION['description']
    
    @pytest.mark.xfail(reason="Текст в тултипах тарифов 'Сонный' и 'Разговорчивый' не соответствуют ТЗ, заведен баг")    
    @allure.title("Тест содержания тултипа для тарифа разговорный")
    def test_tooltip_tarrif_talk_texts(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_talk()
        page.focus_on_button_info()
        actual_title = page.get_info_title()
        actual_description = page.get_info_description()
        
        assert actual_title == Data.TEXT_TARRIF_TALK['title']
        assert actual_description == Data.TEXT_TARRIF_TALK['description']
        
    @allure.title("Тест содержания тултипа для тарифа утешительный")
    def test_tooltip_tarrif_comforting_texts(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_comforting()
        page.focus_on_button_info()
        actual_title = page.get_info_title()
        actual_description = page.get_info_description()
        
        assert actual_title == Data.TEXT_TARRIF_COMFORTING['title']
        assert actual_description == Data.TEXT_TARRIF_COMFORTING['description']
        
    @allure.title("Тест содержания тултипа для тарифа гламурный")
    def test_tooltip_tarrif_glossy_texts(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.click_button_tariff_glossy()
        page.focus_on_button_info()
        actual_title = page.get_info_title()
        actual_description = page.get_info_description()
        
        assert actual_title == Data.TEXT_TARRIF_GLOSSY['title']
        assert actual_description == Data.TEXT_TARRIF_GLOSSY['description']

    @allure.title("Тест наличия полей в экстре")
    @allure.description("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси.")
    def test_extra_fields_visible(self, enter_addresses):
        page = MainPage(enter_addresses)
        page.click_on_button_get_taxi()
        page = GetTaxiPage(enter_addresses)
        
        assert page.get_text_input_phone() == Data.TEXT_EXTRA_PHONE_INPUT
        assert page.get_text_button_payment_method() == Data.TEXT_EXTRA_PAYMENT_SELECT
        assert page.get_text_input_comment() == Data.TEXT_EXTRA_COMMENT_INPUT
        assert page.get_text_title_requirements() == Data.TEXT_EXTRA_REQUIREMENTS_BUTTON
        assert page.get_text_button_get_taxi() == Data.TEXT_EXTRA_GET_TAXI_BUTTON
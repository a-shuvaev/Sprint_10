from pages.get_taxi_page import GetTaxiPage
from data.data import Data
import pytest
import allure

class TestGetTaxiPage:
    
    @allure.title("Тест отображение тарифов такси")
    @allure.description("Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_all_tarrifs_visible(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        
        assert page.compare_list_names_all_tariffs()
    
    @allure.title("Тест активности тарифа")
    @allure.description("Один тариф выделен как активный")
    def test_active_tarrif(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        
        assert page.is_active_tariff_highlighted()
        
    @allure.title("Тест отображения тултипа")
    @allure.description("При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ")
    def test_tooltip_tarrif(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        page.focus_on_button_info()
        
        assert page.is_extra_info_panel_visible()
    
    #Тесты с двумя фейлами, так как текст в тултипах отличается от ТЗ
    @pytest.mark.xfail(reason="Текст в тултипах тарифов 'Сонный' и 'Разговорчивый' не соответствуют ТЗ, заведен баг")
    @pytest.mark.parametrize('click_button_tarrif,get_texts',[
        (GetTaxiPage.click_button_tariff_work, Data.TEXT_TARRIF_WORK),
        (GetTaxiPage.click_button_tariff_sleep, Data.TEXT_TARRIF_SLEEP),
        (GetTaxiPage.click_button_tariff_vacation, Data.TEXT_TARRIF_VACATION),
        (GetTaxiPage.click_button_tariff_talk, Data.TEXT_TARRIF_TALK),
        (GetTaxiPage.click_button_tariff_comforting, Data.TEXT_TARRIF_COMFORTING),
        (GetTaxiPage.click_button_tariff_glossy, Data.TEXT_TARRIF_GLOSSY)
    ])
    @allure.title("Тест содержания тултипа для каждого тарифа")
    def test_tooltip_tarrif_texts(self, open_panel_tarrif_taxi, click_button_tarrif, get_texts):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        click_button_tarrif(page)
        page.focus_on_button_info()
        actual_title = page.get_info_title()
        actual_description = page.get_info_description()
        
        assert (actual_title == get_texts['title'] and
                actual_description == get_texts['description']), f"Фактический заголовок: {actual_title}, ожидаемый заголовок: {get_texts['title']}. Фактическое описание: {actual_description}, ожидаемое описание: {get_texts['description']}"
        
    @allure.title("Тест наличия полей в экстре")
    @allure.description("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси.")
    def test_extra_fields_visible(self, open_panel_tarrif_taxi):
        page = GetTaxiPage(open_panel_tarrif_taxi)
        
        assert (page.get_text_input_phone() == Data.TEXT_EXTRA_PHONE_INPUT and
                page.get_text_button_payment_method() == Data.TEXT_EXTRA_PAYMENT_SELECT and
                page.get_text_input_comment() == Data.TEXT_EXTRA_COMMENT_INPUT and
                page.get_text_title_requirements() == Data.TEXT_EXTRA_REQUIREMENTS_BUTTON and
                page.get_text_button_get_taxi() == Data.TEXT_EXTRA_GET_TAXI_BUTTON)
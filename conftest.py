from pages.main_page import MainPage
from pages.get_taxi_page import GetTaxiPage
from pages.search_taxi_form import SearchTaxiFormPage
from pages.finish_order_taxi_page import FinishOrderTaxiPage
from data.data import Data
from data.urls import Urls
from selenium import webdriver
import pytest
import allure


@allure.title("Настройка и завершение работы драйвера")
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@allure.title("Ввод адресов")
@pytest.fixture()
def enter_addresses(driver):
    page = MainPage(driver)
    page.input_address_from(Data.ADDRESS_FROM)
    page.input_address_to(Data.ADDRESS_TO)
    yield driver


@allure.title("Выбор самоката")
@pytest.fixture()
def choose_scooter_route(enter_addresses):
    page = MainPage(enter_addresses)
    page.click_tab_self()
    page.click_option_scooter()
    yield enter_addresses


@allure.title("Открытие страницы выбора такси")
@pytest.fixture()
def open_panel_tarrif_taxi(enter_addresses):
    page = MainPage(enter_addresses)
    page.click_tab_fast()
    page.click_on_button_get_taxi()
    yield enter_addresses


@allure.title("Открытие формы поиска такси")
@pytest.fixture()
def open_search_taxi_form(open_panel_tarrif_taxi):
    page = GetTaxiPage(open_panel_tarrif_taxi)
    page.click_button_tariff_work()
    page.click_icon_arrow_requirements()
    page.switch_laptop_table()
    page.click_button_get_taxi()
    yield open_panel_tarrif_taxi


@allure.title("Открытие формы завершения заказа такси")
@pytest.fixture()
def open_finish_order_taxi_form(open_search_taxi_form):
    page = SearchTaxiFormPage(open_search_taxi_form)
    page.wait_timer_end()
    page = FinishOrderTaxiPage(open_search_taxi_form)
    page.is_picture_car_driver_visible()
    yield open_search_taxi_form


@allure.title("Открытие формы завершения заказа с запоминанием цены поездки")
@pytest.fixture()
def open_finish_order_taxi_form_with_price(open_panel_tarrif_taxi):
    page = GetTaxiPage(open_panel_tarrif_taxi)
    page.click_button_tariff_work()
    cost = page.get_text_price_info()
    page.click_button_get_taxi()
    page = SearchTaxiFormPage(open_panel_tarrif_taxi)
    page.wait_timer_end()
    page = FinishOrderTaxiPage(open_panel_tarrif_taxi)
    page.is_picture_car_driver_visible()
    yield open_panel_tarrif_taxi, cost

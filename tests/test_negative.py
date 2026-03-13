import allure
from allure_commons.types import Severity
from data.users import User, Gender, Hobbies
from pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("owner", "timofeevaao")
@allure.feature("Сравнение данных")
@allure.story("Данные")
def test_guru_hw_13():

    a = 1
    b = -1
    assert a == b, 'Данные не совпадают'
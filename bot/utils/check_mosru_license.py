from bot.config import *
from bot.services.mosru_license import (CarLicense, CarierLicense)


def check_car_license(driver, car_number):
    """mosru лицензия на машину"""
    url = MOSRU_CAR_LICENSE_URL.format(car_number)
    try:
        license = CarLicense(driver, url, car_number)
        license_data = license.extract_license_data()
        if license_data["Статус"].strip() == "Действующий":
            return True
    except:
        return False


def check_carier_license(driver, car_number):
    """mosru лицензия на перевозчика"""
    url = MOSRU_CARIER_LICENSE_URL.format(car_number)
    try:
        license = CarierLicense(driver, url, car_number)
        license_data = license.extract_license_data()
        print(license_data["Статус:"].strip())
        if license_data["Статус"].strip() == "Действующий":
            return True
    except:
        return False

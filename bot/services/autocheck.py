import asyncio
import schedule

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bot.config import *
from bot.db import db
from bot.utils import (check_mosreg_license, check_mosru_license)



def check_car_license(driver, car_number) -> bool:
    """Проверяем лицензию на машину"""
    if check_mosreg_license.check_car_license(driver, car_number):
        db.add_region_to_db("Московская область", car_number)
        return True
    elif check_mosru_license.check_car_license(driver, car_number):
        db.add_region_to_db("Москва", car_number)
        return True
    else:
        return False


def check_carier_license(driver, car_number) -> bool:
    """Проверяем лицензию на перевозчка"""
    inn_number = db.get_inn_number(car_number)
    if inn_number is not None:
        return check_mosreg_license.check_carier_license(driver, inn_number)
    if check_mosru_license.check_carier_license(driver, car_number):
        return True
    return False


def check_licenses():
    """Проверяем лицензию по номеру машины"""
    car_number_list = db.get_car_numbers()
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    for car_number in car_number_list:
        car_number = car_number[0].strip()
        #Если лицензия гна машину есть
        if check_car_license(driver, car_number):
            #Проверяем лицензию на перевозчка
            if check_carier_license(driver, car_number):
                #Если она тоже есть, то ставим статус Ready
                db.add_license_status(car_number, "Ready")
            else:
                #Если нет, ставим статус Car (вышла только на машину)
                db.add_license_status(car_number, "Car")
    driver.quit()


async def start_checking():
    #schedule.every().day.at("09:55").do(check_licenses)
    #schedule.every().day.at("14:20").do(check_licenses)
    #schedule.every().day.at("17:20").do(check_licenses)
    while True:
        check_licenses()
        #schedule.run_pending()
        await asyncio.sleep(500)



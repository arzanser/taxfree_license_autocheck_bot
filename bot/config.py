import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = str(os.getenv("TELEGRAM_BOT_TOKEN"))
CAPTCHA_TOKEN = str(os.getenv("CAPTCHA_TOKEN"))
CHANNEL_ID = str(os.getenv("TELEGRAM_CHANNEL"))

DB_PATH = "/Users/arzanser/Dev/Code/Python/taxfree/taxfree_license_autocheck_bot/bot/db/db.db"
CAPTCHA_FILE_PATH = "/Users/arzanser/Dev/Code/Python/taxfree/taxfree_license_autocheck_bot/bot/images/captcha.png"
QR_FILE_PATH = "/Users/arzanser/Dev/Code/Python/taxfree/taxfree_license_autocheck_bot/bot/images/qr.png"
CAR_NUMBER_LIST_PATH = "/Users/arzanser/Dev/Code/Python/taxfree/taxfree_license_autocheck_bot/bot/car_number_list.txt"

MOSREG_CAR_LICENSE_URL = "https://mtdi.mosreg.ru/taxi-cars?licenseNumber=&inn=&name=&gosNumber={}&region=ALL"
MOSREG_CARIER_LICENSE_URL = "https://mtdi.mosreg.ru/taxi-permits?licenseNumber=&inn={}&name=&region=ALL"
MOSRU_CAR_LICENSE_URL = "https://transport.mos.ru/auto/reestr_taxi"
MOSRU_CARIER_LICENSE_URL = "https://transport.mos.ru/auto/reestr_carrier"

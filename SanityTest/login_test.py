from helper_base import HelperBase
from test_name import TestNames
from config import Config


def loginfirsttest():
    HelperBase.print_starting_message(TestNames.LOGIN_TEST)
    HelperBase.get_driver_and_configure_browser_and_url(Config.SERVER_URL, is_headless=False, reset=0)
    HelperBase.login_to_commbox(Config.ADMIN_BRAND, Config.ADMIN_USER, Config.ADMIN_PASSWORD)


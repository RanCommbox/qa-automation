from SanityTest.helper_base import HelperBase
from SanityTest.test_name import TestNames
from SanityTest.config import Config


def loginfirsttest():
    HelperBase.print_starting_message(TestNames.LOGIN_TEST)
    HelperBase.get_driver_and_configure_browser_and_url(Config.SERVER_URL, is_headless=True, reset=0)
    HelperBase.login_to_commbox(Config.ADMIN_BRAND, Config.ADMIN_USER, Config.ADMIN_PASSWORD)


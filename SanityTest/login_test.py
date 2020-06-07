from SanityTest.helper_base import HelperBase
from SanityTest.test_name import TestNames
from SanityTest.config import Config
import unittest
import sys, os


class TestLogin(unittest.TestCase):
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')

    def test_login(self):
        HelperBase.print_starting_message(TestNames.LOGIN_TEST)
        HelperBase.get_driver_and_configure_browser_and_url(Config.SERVER_URL, is_headless=False, reset=0)
        HelperBase.login_to_commbox(Config.ADMIN_BRAND, Config.ADMIN_USER, Config.ADMIN_PASSWORD)

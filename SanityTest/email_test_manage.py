from lib2to3.pgen2 import driver

from SanityTest.helper_base import HelperBase
from SanityTest.test_name import TestNames
from SanityTest.config import Config
import unittest
import sys, os


class TestEmailFromManage(unittest.TestCase):
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')

    def test_mail_from_manage(self):
        HelperBase.print_starting_message(TestNames.LOGIN_TEST)
        HelperBase.get_driver_and_configure_browser_and_url(Config.SERVER_URL, is_headless=False, reset=0)
        HelperBase.sending_email_from_mange(Config.ADMIN_BRAND, Config.ADMIN_USER, Config.ADMIN_PASSWORD, self)









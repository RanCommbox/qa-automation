import pytest
from config import Config
from helper_base import HelperBase
from test_name import TestNames


@pytest.yield_fixture
def before_after_test_actions(is_headless):
    HelperBase.get_driver_and_configure_browser_and_url(Config.SERVER_URL, is_headless, False)
    HelperBase.login_to_commbox(Config.ADMIN_USER, Config.ADMIN_PASSWORD, Config.ADMIN_BRAND)
    yield
    if is_headless is not 'True':
        HelperBase.close_browser_window()

import requests
import unittest
import sys, os


class ApiTesting(unittest.TestCase):
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')

    def test_get_state(self):
        response = requests.get("https://api.commboxtest.com/core/systemstatus?"
                                "access_token=55cdabc3e5c84d32857c5a61ef7f76ee")
        assert response.status_code == 400

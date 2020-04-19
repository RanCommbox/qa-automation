import requests
import unittest

class ApiTesting(unittest.TestCase):


    def test_get_state(self):
        response = requests.get("https://api.commboxtest.com/core/systemstatus?"
                                "access_token=55cdabc3e5c84d32857c5a61ef7f76ee")
        assert response.status_code == 400

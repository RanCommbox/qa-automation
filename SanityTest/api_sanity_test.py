import requests
import unittest
import sys, os


class ApiTesting(unittest.TestCase):
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')

    def test_get_state(self):
        response = requests.get("https://api.commbox.io/status")
        assert response.status_code == 200

    def test_get_manager(self):
        response = requests.get("https://api.commbox.io/managers/13218299?access_token=55cdabc3e5c84d32857c5a61ef7f76ee")
        assert response.status_code == 200

    def test_change_object_status(self):
        response = requests.post("https://api.commbox.io/objects/19048555/status/"
                                "2?access_token=55cdabc3e5c84d32857c5a61ef7f76ee")
        assert response.status_code == 200

    def test_send_whatsapp_from_manage(self):
        url = "https://api.commbox.io/whatsapp/sendtemplatedmessage/" \
              "l8I6ShrhRC_bEkTEZyj32DQ%3d%3d?access_token=55cdabc3e5c84d32857c5a61ef7f76ee"

        payload = "{\"recipient\": \"+972524472334\",\n\"template_name\": \"followup_after_24h\"," \
                  "\n\"language\": {\n\"code\": \"en_US\"\n},\n\"localizable_params\":" \
                  " [\n{\n\"default\": \"testapi\"\n}\n],\n\"validate\": true\n}"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

    def send_sms_from_the_manage(self):
        url = "https://api.commbox.io/sms/sendsms/uCjO85DEmfmwVX26vtW1_bw%3d%3d?access_token=55cdabc3e5c84d32857c5a61ef7f76ee"

        payload = "{\n    \"data\": {\n        \"Number\": \"972524472334\",\n        \"Message\": \"היי חדש טסט API\"\n    }\n}"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

    def rest_get_user_send_otp_tmura(self):
        url = "https://www.tmuralife.co.il/WebApiProd/BumpyardApi/IsCustomerValid/" \
              "748d088f653b440498b13928f9c9870b/0526339939/12312310?contentType=application/json"

        payload = {}
        headers = {
            'Cookie': 'TS01912bf0=017a295a5cad35a3a1206f25ca4fed874726468153c76dd2fd6'
                      '848b798c8a140fc53bd4c7013449dd93b5267eb78c1c23891094678'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

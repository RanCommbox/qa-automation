from SanityTest.helper_base import HelperBase
from SanityTest.test_name import TestNames
from SanityTest.config import Config
import unittest
import sys, os
import smtplib
from email.mime.text import MIMEText
from  email.header import Header
from socket import gaierror

class TestEmailFromUser(unittest.TestCase):
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')

    def test_email_user(self):

        from_addres = "ran.ya@commbox.io"
        login_to_mail = from_addres
        email_password = "Aa123456!"
        to_addres = ["dantest@commboxtest.com"]
        subject = "Ran Automation test"

        msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
               % (from_addres, ", ".join(to_addres), subject))
        msg += "some text\r\n"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(login_to_mail, email_password)
        server.sendmail(from_addres, to_addres, msg)
        server.quit()

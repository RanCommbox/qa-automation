from unittest import TestLoader, TestSuite, TextTestRunner
import sys, os
import unittest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from SanityTest.login_test import TestLogin
from SanityTest.email_test_user import TestEmailFromUser
from SanityTest.email_test_manage import TestEmailFromManage
from SanityTest.api_sanity_test import ApiTesting




api_first_test = TestLoader().loadTestsFromTestCase(ApiTesting)
login_testing = TestLoader().loadTestsFromTestCase(TestLogin)
email_testing_user = TestLoader().loadTestsFromTestCase(TestEmailFromUser)
email_testing_mange = TestLoader().loadTestsFromTestCase(TestEmailFromManage)
suite = TestSuite(email_testing_mange)
runner = TextTestRunner(verbosity=2)
runner.run(suite)

#suite1 = unittest.TestLoader().loadTestsFromTestCase(Login)
#suite2 = unittest.TestLoader().loadTestsFromTestCase(ApiTesting)
#alltests = unittest.TestSuite([suite1, suite2])

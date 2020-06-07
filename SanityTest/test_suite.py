from unittest import TestLoader, TestSuite, TextTestRunner
import sys, os
import unittest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from SanityTest.login_test import TestLogin

#suite = unittest.TestLoader().loadTestsFromTestCase(test_get_state()
#unittest.TextTestRunner(verbosity=2).run(suite)


#api_first_test = TestLoader().loadTestsFromTestCase(ApiTesting)
login_testing = TestLoader().loadTestsFromTestCase(TestLogin)

suite = TestSuite(login_testing)
runner = TextTestRunner(verbosity=2)
runner.run(suite)

#suite1 = unittest.TestLoader().loadTestsFromTestCase(Login)
#suite2 = unittest.TestLoader().loadTestsFromTestCase(ApiTesting)
#alltests = unittest.TestSuite([suite1, suite2])

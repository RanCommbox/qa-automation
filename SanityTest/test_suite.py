import unittest
from unittest import TestLoader, TestSuite, TextTestRunner

import SanityTest.api_sanity_test
from SanityTest.login_test import loginfirsttest
from SanityTest.api_sanity_test import ApiTesting

#suite = unittest.TestLoader().loadTestsFromTestCase(test_get_state()
#unittest.TextTestRunner(verbosity=2).run(suite)



first_test = TestLoader().loadTestsFromTestCase(ApiTesting)
suite = TestSuite(first_test)
runner = TextTestRunner()
runner.run(suite)
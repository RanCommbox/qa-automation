import unittest

from login_test import loginfirsttest


suite = unittest.TestLoader().loadTestsFromTestCase(loginfirsttest())
unittest.TextTestRunner(verbosity=2).run(suite)
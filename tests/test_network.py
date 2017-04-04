import os
import unittest
from ..network import InternetConnection

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_internet_connection(self):
        status_code = InternetConnection().check_internet()
        self.assertTrue(status_code == 200)

    def test_app_is_testing(self):
        self.assertFalse(True == False)

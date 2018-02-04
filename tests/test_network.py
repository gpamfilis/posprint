# coding: utf-8
import os
import unittest
from ..network import InternetConnection
from ..posprint_v2 import create_deltio

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_internet_connection(self):
        status_code = InternetConnection().check_internet()
        self.assertTrue(status_code == 200)

    # def test_create_deltio(self):
    #     create_deltio(1)
    #     self.assertTrue(True == False)

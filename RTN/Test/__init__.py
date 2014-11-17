__author__ = 'Daniel'
from unittest import TestSuite
from Test import test_connection
from Test import test_listener
from Test import test_parser
from Test import test_SNMPv2

class AlleTests(TestSuite):

    def __init__(self):
        x = test_connection.TestConnection()
        self.addTest(x)

suite = AlleTests()
suite.run()

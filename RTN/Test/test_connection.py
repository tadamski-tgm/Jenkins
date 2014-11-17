from unittest import TestCase
from Control.Connection import Connection

__author__ = 'Daniel Bracher'


class TestConnection(TestCase):

    def test_checkConnection_RightParams(self):
        con = Connection
        self.assertTrue(con.checkConnection(con, "10.0.100.10", 161, "5xHIT"))

    def test_checkConnection_WrongIP(self):
        con = Connection
        self.assertFalse(con.checkConnection(con, "xxx", 161, "5xHIT"))

    #Works, but commented because of delay to server
    """def test_checkConnection_WrongPort(self):
        con = Connection
        self.assertFalse(con.checkConnection(con, "10.0.100.10", 0, "5xHIT"))"""

    #Works, but commented because of delay to server
    """def test_checkConnection_WrongComName(self):
        con = Connection
        self.assertFalse(con.checkConnection(con, "10.0.100.10", 0, "xxx"))"""

    def test_getOIDTable(self):
        self.fail()

    """def test_getOID(self):
        self.fail()

    def test_getMIB(self):
        self.fail()"""
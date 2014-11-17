from unittest import TestCase
from Control.Connection import SNMPv3
from pysnmp.smi.error import SmiError


'''
@date: 29.10.2014
@author: Daniel Bracher
@description: Tests the Class SNMPv3 by checking
    -if getMIB and getMIBTable works when inputs are given rightly
    -if errors occur when given wrong mibfile or wrong oid
'''


class TestSNMPv3(TestCase):

    def test_getMIB_RightInput(self):
        snmp = SNMPv3
        result = snmp.getMIB(snmp,'SNMPv2-MIB', 'sysName',0,'5xHIT', '10.0.100.10', 161)
        #expects None because NetScreen doesnt supports v3
        expected = None
        self.assertEquals(result, expected)

    def test_getMIBTable_RightInput(self):
        snmp = SNMPv3
        result = snmp.getMIBTable(snmp,'NETSCREEN-POLICY-MIB','nsPlySrcAddr','5xHIT','10.0.100.10',161)
        #expects None because NetScreen doesnt supports v3
        expected = None
        self.assertEqual(result, expected)

    def test_getMIB_wrongMIBFile(self):
        with self.assertRaises(SmiError):
            snmp = SNMPv3
            result = snmp.getMIB(snmp,'Fail', 'sysName',0,'5xHIT', '10.0.100.10', 161)
            expected = "rockthenet"
            self.assertEquals(result, expected)

    def test_getMIB_wrongOID(self):
        with self.assertRaises(SmiError):
            snmp = SNMPv3
            result = snmp.getMIB(snmp,'NETSCREEN-POLICY-MIB', 'fail',0,'5xHIT', '10.0.100.10', 161)
            expected = "rockthenet"
            self.assertEquals(result, expected)
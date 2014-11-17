from unittest import TestCase
from Control.Parser import Parser
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp import error
from socket import gaierror

'''
@date: 29.10.2014
@author: Daniel Bracher
@description: Tests the Class PARSER by checking
    -if it returns the right output, when right input given
    -if it returns an error when nputting wrong ip, port or oid
'''


class TestParser(TestCase):

    def test_parseData_CorrectInput_OneDimensional(self):
            par = Parser()
            cmdGen = cmdgen.CommandGenerator()

            errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.getCmd (
                cmdgen.CommunityData('public', "5xHIT"),
                cmdgen.UdpTransportTarget(("10.0.100.10", 161)),
                cmdgen.MibVariable('SNMPv2-MIB', 'sysName', 0).addMibSource('MIB/')
            )

            result = par.parseData(errorIndication, errorStatus, errorIndex, varBindTable, 1)
            expected = "rockthenet"
            self.assertEquals(result, expected)

    def test_parseData_CorrectInput_TwoDimensional(self):
            par = Parser()
            cmdGen = cmdgen.CommandGenerator()

            errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd (
                cmdgen.CommunityData('public', "5xHIT"),
                cmdgen.UdpTransportTarget(("10.0.100.10", 161)),
                cmdgen.MibVariable('NETSCREEN-POLICY-MIB','nsPlySrcAddr').addMibSource('MIB/'),
                lexicographicMode = False, ignoreNonIncreasingOid = False, lookupNames = True
            )

            result = par.parseData(errorIndication, errorStatus, errorIndex, varBindTable, 0)
            expected = ['Any', 'Any', 'Any', 'Any', 'Any', 'Any', 'Any', 'Any', 'Any', 'Any', 'Any']
            self.assertEquals(result, expected)

    def test_parseData_ErrorIndicationSet(self):
        par = Parser()
        result = par.parseData("Error", None, None, None, None)
        self.assertIsNone(result)

    def test_parseData_IPtooLong(self):
        with self.assertRaises(error.PySnmpError):
            par = Parser()
            cmdGen = cmdgen.CommandGenerator()
            errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd (
                cmdgen.CommunityData('public', "5xHIT"),
                cmdgen.UdpTransportTarget(("10.0.100.10.10", 161)), '1.3.6.1.2.1.1.1.0',
                lexicographicMode = False, ignoreNonIncreasingOid = False, lookupNames = True
            )

    def test_parseData_alphabeticalPort(self):
        with self.assertRaises(error.PySnmpError):
            par = Parser()
            cmdGen = cmdgen.CommandGenerator()
            errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd (
                cmdgen.CommunityData('public', "5xHIT"),
                cmdgen.UdpTransportTarget(("10.0.100.10.10", "aaa")), '1.3.6.1.2.1.1.1.0',
                lexicographicMode = False, ignoreNonIncreasingOid = False, lookupNames = True
            )

    def test_parseData_alphabeticalOID(self):
        with self.assertRaises(error.PySnmpError):
            par = Parser()
            cmdGen = cmdgen.CommandGenerator()
            errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd (
                cmdgen.CommunityData('public', "5xHIT"),
                cmdgen.UdpTransportTarget(("10.0.100.10.10", 161)), 'a.a.a.a',
                lexicographicMode = False, ignoreNonIncreasingOid = False, lookupNames = True
            )



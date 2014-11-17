'''
Created on 28.10.2014

@author: ilendemli
'''

from pysnmp.entity.rfc3413.oneliner import cmdgen
from Control.Parser import Parser

class SNMPv2:
    parser = Parser()
    cmdGen = cmdgen.CommandGenerator()
    
    def getMIB(self, mib, obj, index, communityName, ipAddress, ipPort):
        errorIndication, errorStatus, errorIndex, varBindTable = self.cmdGen.getCmd (
            cmdgen.CommunityData(communityName),
            cmdgen.UdpTransportTarget((ipAddress, ipPort)), 
            cmdgen.MibVariable(mib, obj, index).addMibSource('MIB/')
        )

        return self.parser.parseData(errorIndication, errorStatus, errorIndex, varBindTable, 1)

    def getMIBTable(self, mib, obj, communityName, ipAddress, ipPort):
        errorIndication, errorStatus, errorIndex, varBindTable = self.cmdGen.nextCmd (
            cmdgen.CommunityData(communityName),
            cmdgen.UdpTransportTarget((ipAddress, ipPort)),
            cmdgen.MibVariable(mib, obj).addMibSource('MIB/'),
            lexicographicMode = False, ignoreNonIncreasingOid = False, lookupNames = True
        )

        return self.parser.parseData(errorIndication, errorStatus, errorIndex, varBindTable, 0)
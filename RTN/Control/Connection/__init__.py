import socket
import json

from pysnmp.error import PySnmpError

from Control.Connection.SNMPv3 import SNMPv3
from Control.Connection.SNMPv2 import SNMPv2

class Connection:
    snmpv3 = SNMPv3()
    snmpv2 = SNMPv2()
    
    @staticmethod
    def getSNMPVersion(ipAddress, ipPort, communityName):
        try:
            socket.inet_aton(ipPort)
            
            result = Connection.checkV3(communityName, ipAddress, ipPort)
            
            if (result == None):
                result = Connection.checkV2(communityName, ipAddress, ipPort)
                
                if (result == None):
                    # TODO: check snmp v1
                    return -2
                
                else:
                    return 2
            
            else:
                return 3

            return 0
            
        except (socket.error, PySnmpError): 
            return -1
       
    @staticmethod 
    def checkV3(communityName, ipAddress, ipPort):
        return Connection.snmpv3.getMIB('SNMPv2-MIB', 'sysDescr', 0, communityName, ipAddress, ipPort)

    @staticmethod
    def checkV2(communityName, ipAddress, ipPort):
        return Connection.snmpv2.getMIB('SNMPv2-MIB', 'sysDescr', 0, communityName, ipAddress, ipPort)
    
    @staticmethod
    def renderJSON(obj):
        return json.dumps(obj)
    
    @staticmethod
    def getMIBs(session, mib, objs):
        ipAddress = session['ipAddress']
        ipPort = session['ipPort']
        communityName = session['communityName']
        snmp_version = session['snmp_version']
        
        snmp_socket = None
        
        if (snmp_version == 3):
            snmp_socket = SNMPv3()
            
        elif (snmp_version == 2):
            snmp_socket = SNMPv2()
            
        results = {}
        
        for obj in objs:
            result = snmp_socket.getMIBTable(mib, obj[1], communityName, ipAddress, ipPort)
            results[obj[0]] = result

        return Connection.renderJSON(results)
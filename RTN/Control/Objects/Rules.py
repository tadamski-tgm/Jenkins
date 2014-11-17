'''
Created on 30.10.2014

@author: ilendemli
'''

from Control.Connection import Connection

class Rules:
    objs = [
            ['id', 'nsPlyId'], 
            ['vsys', 'nsPlyVsys'],
            ['srczone', 'nsPlySrcZone'],
            ['dstzone', 'nsPlyDstZone'],
            ['srcaddr', 'nsPlySrcAddr'],
            ['dstaddr', 'nsPlyDstAddr'],
            ['service', 'nsPlyService'],
            ['action', 'nsPlyAction'],
            ['nat', 'nsPlyNat'],
            ['fixport', 'nsPlyFixPort'],
            ['dipid', 'nsPlyDipId'],
            ['activestatus', 'nsPlyActiveStatus'],
            ['name', 'nsPlyName'],
            ['servicename', 'nsPlyServiceName']
            ]
    
    @staticmethod
    def getData(session):
        return Connection.getMIBs(session, 'NETSCREEN-POLICY-MIB', Rules.objs)
        
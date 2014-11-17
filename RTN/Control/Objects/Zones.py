'''
Created on 30.10.2014

@author: ilendemli
'''
from Control.Connection import Connection

class Zones:
    objs = [
            ['id', 'nsZoneCfgId'], 
            ['name', 'nsZoneCfgName'], 
            ['type', 'nsZoneCfgType'], 
            ['vsys', 'nsZoneCfgVsys']
            ]
    
    @staticmethod
    def getData(session):
        return Connection.getMIBs(session, 'NETSCREEN-ZONE-MIB', Zones.objs)
        
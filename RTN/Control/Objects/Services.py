'''
Created on 30.10.2014

@author: ilendemli
'''
from Control.Connection import Connection

class Services:
    objs = [
            ['index', 'nsServiceIndex'], 
            ['name', 'nsServiceName'],
            ['category', 'nsServiceCategory']
            ]
    
    @staticmethod
    def getData(session):
        return Connection.getMIBs(session, 'NETSCREEN-SERVICE-MIB', Services.objs)
        